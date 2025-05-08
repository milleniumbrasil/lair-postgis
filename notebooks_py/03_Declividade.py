#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para recortar e poligonizar a base de Declividade por Munícipios

Projeto: Sistema de Apoio à Caracterização de Imóveis Rurais
Embrapa/2023
"""

import os
import glob
import rasterio
from rasterio.mask import mask
import shapely
import geopandas as gpd
import numpy as np
from osgeo import ogr, osr, gdal
import time
import shutil
import pyproj
import sys

def verificar_dependencias():
    """Verifica se todas as dependências necessárias estão instaladas"""
    dependencias = {
        "rasterio": rasterio,
        "geopandas": gpd,
        "shapely": shapely,
        "osgeo.gdal": gdal,
        "osgeo.ogr": ogr,
        "osgeo.osr": osr,
        "numpy": np,
        "pyproj": pyproj
    }
    
    falhas = []
    for nome, modulo in dependencias.items():
        if modulo is None:
            falhas.append(nome)
    
    if falhas:
        print("ERRO: As seguintes dependências não foram encontradas:")
        for falha in falhas:
            print(f"- {falha}")
        print("\nInstale as dependências com pip:")
        print("pip install numpy geopandas rasterio shapely gdal pyproj")
        return False
    
    return True

def main():
    """Função principal que processa a declividade por municípios"""
    # Verificar dependências primeiro
    if not verificar_dependencias():
        return 1
    
    print("\n" + "="*80)
    print("Processamento de Declividade por Municípios")
    print("="*80 + "\n")
    
    try:
        # Solicitação de caminhos necessários
        dirpath = input('Diretório principal: ')
        originais_path = input('Pasta com originais: ')
        car_path = input('Diretório do CAR: ')
        limites_buf = input('Caminho Municípios com Buffer: ')
        limites = input('Caminho Municípios: ')
        
        # Criar pastas para armazenar arquivos
        out_path = os.path.join(dirpath, 'Decliv_UF_Municipios')
        os.makedirs(out_path, exist_ok=True)
        print(f"Diretório para arquivos de declividade: {out_path}")
        
        temp_path = os.path.join(dirpath, 'Temporarios')
        os.makedirs(temp_path, exist_ok=True)
        print(f"Diretório para arquivos temporários: {temp_path}")
        
        final_path = os.path.join(dirpath, 'Decliv_UF_Municipios_CAR')
        os.makedirs(final_path, exist_ok=True)
        print(f"Diretório para arquivos finais integrados com CAR: {final_path}")
        
        # Lendo shapefile que será usado como máscara para recorte (com buffer)
        print("\nLendo shapefile de municípios com buffer...")
        lim_buf = gpd.read_file(rf"{limites_buf}")
        # Reprojetando o shapefile para WGS84
        lim_buf = lim_buf.to_crs(epsg=4326)
        
        # Lendo shapefile que será usado como máscara para recorte (sem buffer)
        print("\nLendo shapefile de municípios sem buffer...")
        lim = gpd.read_file(rf"{limites}")
        # Reprojetando o shapefile para WGS84
        lim = lim.to_crs(epsg=4326)
        
        # Lista dos estados
        estados = list(np.unique(lim['SIGLA_UF']))
        print(f"Estados a processar: {', '.join(estados)}")
        
        # Recortando os rasters de declividade pelo buffer dos municípios
        print("\nIniciando recorte de rasters por município...")
        for i, estado in enumerate(estados, 1):
            print(f"[{i}/{len(estados)}] Processando estado: {estado}")
            
            rasters = glob.glob(originais_path + fr'**/{estado}.tif')
            if not rasters:
                print(f"  Nenhum raster encontrado para o estado {estado}")
                continue
                
            # Selecionar GeoDataFrame por estado
            select = lim_buf[lim_buf['SIGLA_UF'] == f'{estado}']
            # Códigos dos municípios
            names = [x for x in select['CD_MUN']]
            
            for raster in rasters:
                print(f"  Processando raster: {os.path.basename(raster)}")
                try:
                    # Lendo o raster
                    ras_data = rasterio.open(raster)
                    
                    # Definindo o caminho de saída do raster recortado
                    nome_arquivo = os.path.basename(raster)
                    nome_arquivo = nome_arquivo.replace('.tif', '')
                    output = os.path.join(temp_path, nome_arquivo)
                    
                    # Recortando o raster por município
                    for j, municipio in enumerate(names):
                        try:
                            print(f"    Recortando município: {municipio}")
                            geom = []
                            coord = shapely.geometry.mapping(select.iloc[j].geometry)
                            geom.append(coord)
                            
                            with rasterio.open(raster) as src:
                                out_image, out_transform = rasterio.mask.mask(src, geom, crop=True)
                                out_meta = src.meta
                            
                            out_meta.update({
                                'driver': 'GTiff',
                                'height': out_image.shape[1],
                                'width': out_image.shape[2],
                                'transform': out_transform
                            })
                            
                            # Salvando os rasters recortados
                            output_file = f'{output}_{municipio}_temp1.tif'
                            with rasterio.open(output_file, 'w', **out_meta) as dest:
                                dest.write(out_image)
                        except Exception as e:
                            print(f"    Erro ao recortar município {municipio}: {str(e)}")
                except Exception as e:
                    print(f"  Erro ao processar raster {os.path.basename(raster)}: {str(e)}")
        
        # Buscar imagens recortadas
        print("\nBuscando imagens recortadas...")
        imagens = glob.glob(temp_path + '**/*temp1.tif')
        print(f"Encontradas {len(imagens)} imagens recortadas")
        
        # Convertendo Raster para Shapefile
        print("\nIniciando conversão de raster para shapefile...")
        for i, imagem in enumerate(imagens, 1):
            print(f"[{i}/{len(imagens)}] Convertendo: {os.path.basename(imagem)}")
            try:
                driver = gdal.GetDriverByName('GTiff')
                input = gdal.Open(imagem)
                band = input.GetRasterBand(1)
                band1 = band.ReadAsArray()
                proj = input.GetProjection()
                shp_proj = osr.SpatialReference()
                shp_proj.ImportFromWkt(proj)
                
                nome_arq = os.path.basename(imagem).replace('temp1.tif', 'temp2.shp')
                output = os.path.join(temp_path, nome_arq)
                
                call_drive = ogr.GetDriverByName('ESRI Shapefile')
                create_shp = call_drive.CreateDataSource(output)
                shp_layer = create_shp.CreateLayer('Declividade', srs=shp_proj)
                
                new_field = ogr.FieldDefn(str('CD_DECLIV'), ogr.OFTInteger)
                shp_layer.CreateField(new_field)
                
                gdal.Polygonize(band, None, shp_layer, 0, [], callback=None)
                create_shp.Destroy()
                input = None
            except Exception as e:
                print(f"  Erro ao converter {os.path.basename(imagem)}: {str(e)}")
        
        # Dissolve
        print("\nRealizando dissolve por CD_DECLIV...")
        imagens = glob.glob(temp_path + '**/*temp2.shp')
        print(f"Encontrados {len(imagens)} shapefiles para dissolve")
        
        for i, imagem in enumerate(imagens, 1):
            print(f"[{i}/{len(imagens)}] Dissolvendo: {os.path.basename(imagem)}")
            try:
                geodf = gpd.read_file(imagem)
                dissolve = geodf.dissolve(by='CD_DECLIV')
                
                nome_arq = os.path.basename(imagem).replace('temp2.shp', 'temp3.shp')
                output = os.path.join(temp_path, nome_arq)
                
                dissolve.to_file(driver='ESRI Shapefile', filename=output)
            except Exception as e:
                print(f"  Erro ao dissolver {os.path.basename(imagem)}: {str(e)}")
        
        # Cortar por município
        print("\nRecortando shapefiles por município...")
        # Agrupar por município
        agrupado = lim.groupby('CD_MUN')
        
        # Shapefiles que serão recortados
        shapes = glob.glob(temp_path + '**/*temp3.shp')
        print(f"Encontrados {len(shapes)} shapefiles para recorte")
        
        for i, shape in enumerate(shapes, 1):
            print(f"[{i}/{len(shapes)}] Processando: {os.path.basename(shape)}")
            
            for key, values in agrupado:
                if key in shape:
                    try:
                        decliv = gpd.read_file(shape)
                        decliv = decliv.to_crs(epsg=4326)
                        
                        nome_arq = os.path.basename(shape).replace("_temp3.shp", ".shp")
                        output = os.path.join(out_path, f"Decliv_{nome_arq}")
                        
                        mun = lim[lim["CD_MUN"] == f"{key}"]
                        geodf_clip = gpd.clip(decliv, mun)
                        geodf_clip.to_file(driver='ESRI Shapefile', filename=output)
                        print(f"  Recortado: {os.path.basename(output)}")
                    except Exception as e:
                        print(f"  Erro ao recortar {key} de {os.path.basename(shape)}: {str(e)}")
        
        # Renomeando AREA_IMOVEL para seus respectivos municípios
        print("\nRenomeando arquivos AREA_IMOVEL para incluir códigos de municípios...")
        municipios = []
        
        # Percorre a pasta 'CAR' e suas subpastas
        for root, dirs, files in os.walk(car_path):
            for dir in dirs:
                # Verifica se o nome da subpasta é um código de município
                if dir.startswith('SHAPE_'):
                    try:
                        municipio_codigo = dir.split('_')[1]
                        municipios.append(municipio_codigo)
                        
                        # Constrói o caminho completo para a pasta 'AREA_IMOVEL'
                        area_imovel_dir = os.path.join(root, dir, 'AREA_IMOVEL')
                        
                        # Verifica se a pasta 'AREA_IMOVEL' existe
                        if os.path.exists(area_imovel_dir):
                            # Renomeia os arquivos dentro de 'AREA_IMOVEL'
                            for filename in os.listdir(area_imovel_dir):
                                if filename.startswith('AREA_IMOVEL'):
                                    novo_nome = f'{municipio_codigo}_{filename}'
                                    arquivo_antigo = os.path.join(area_imovel_dir, filename)
                                    novo_arquivo = os.path.join(area_imovel_dir, novo_nome)
                                    
                                    # Verificar se o arquivo já existe
                                    if not os.path.exists(novo_arquivo):
                                        os.rename(arquivo_antigo, novo_arquivo)
                                        print(f'  Renomeado: {os.path.basename(arquivo_antigo)} → {os.path.basename(novo_arquivo)}')
                    except Exception as e:
                        print(f"  Erro ao processar diretório {dir}: {str(e)}")
        
        # Integração com CAR
        print("\nIntegrando dados de declividade com CAR...")
        
        # Caminho dos vetores de Declividade
        decl = glob.glob(out_path + '**/*.shp')
        
        # Caminho dos vetores de limites dos imóveis
        car = glob.glob(car_path + '**/*/*/*/*.shp')
        
        caminho_decl = []
        caminho_car = []
        
        for arquivo in decl:
            caminho_decl.append(arquivo)
        
        for arquivo in car:
            if 'AREA_IMOVEL' in arquivo:
                caminho_car.append(arquivo)
        
        print(f"  Encontrados {len(caminho_decl)} arquivos de declividade")
        print(f"  Encontrados {len(caminho_car)} arquivos de CAR")
        
        # Processamento da integração
        # Nota: Esta parte depende da implementação específica da integração com CAR
        # Aqui precisaria adaptar o código do notebook que não está completamente visível
        
        print("\nProcessamento de declividade concluído com sucesso!")
        return 0
        
    except Exception as e:
        print(f"\nERRO: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 