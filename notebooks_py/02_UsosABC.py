#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para gerar a base de Usos ABC por ano e por município

Projeto: Sistema de Apoio à Caracterização de Imóveis Rurais
Embrapa/2023
"""

import os
import glob
import time
import shutil
import numpy as np
import geopandas as gpd
import rasterio
from rasterio.mask import mask
import shapely
from osgeo import ogr, osr, gdal
import pyproj
import sys

def verificar_dependencias():
    """Verifica se todas as dependências estão instaladas corretamente."""
    dependencias = {
        "numpy": np,
        "geopandas": gpd,
        "rasterio": rasterio,
        "shapely": shapely,
        "osgeo.gdal": gdal,
        "osgeo.ogr": ogr,
        "osgeo.osr": osr,
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
    """Função principal que executa a geração de Usos ABC."""
    # Verificar dependências primeiro
    if not verificar_dependencias():
        return 1
    
    print("\n" + "="*80)
    print("Geração da base de Usos ABC por ano e por município")
    print("="*80 + "\n")
    
    try:
        # Solicitação de caminhos necessários
        dirpath = input('Diretório principal: ')
        originais_path = input('Pasta com originais: ')
        limites_buf = input('Caminho Municípios com Buffer: ')
        limites = input('Caminho Municípios: ')
        car_path = input('Diretório do CAR: ')
        
        # Definindo anos de Usos ABC
        anos = ['1985', '2008', '2009', '2010', '2011', '2012', '2013', '2014', 
                '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        
        # Criar pastas para armazenar arquivos temporários e finais
        temp_path = os.path.join(dirpath, 'Temporarios')
        os.makedirs(temp_path, exist_ok=True)
        print(f"Diretório para arquivos temporários: {temp_path}")
        
        out_path = os.path.join(dirpath, 'Usos_ABC_Municipios')
        os.makedirs(out_path, exist_ok=True)
        print(f"Diretório para arquivos finais: {out_path}")
        
        # Criar diretórios para cada ano
        for ano in anos:
            os.makedirs(os.path.join(out_path, ano), exist_ok=True)
        
        # Lendo shapefile que será usado como máscara para recorte
        print("\nLendo shapefile de municípios com buffer...")
        lim_buf = gpd.read_file(rf"{limites_buf}")
        
        print("\nLendo shapefile de municípios sem buffer...")
        lim = gpd.read_file(rf"{limites}")
        
        # Códigos dos municípios
        names = [x for x in lim_buf['CD_MUN']]
        
        # Listar imagens a serem recortadas
        print("\nProcurando imagens para recorte...")
        imagens = glob.glob(originais_path + '**/*.tif')
        print(f"Encontradas {len(imagens)} imagens para processamento")
        
        # Recortando os rasters do Mapbiomas por Município
        print("\nIniciando recorte de rasters por município...")
        for i, raster in enumerate(imagens, 1):
            print(f"[{i}/{len(imagens)}] Processando: {os.path.basename(raster)}")
            
            # Lendo o raster
            ras_data = rasterio.open(raster)
            
            # Definindo o caminho de saída do raster recortado
            nome_arquivo = os.path.basename(raster)
            nome_arquivo = nome_arquivo.replace('.tif', '')
            output = os.path.join(temp_path, nome_arquivo)
            
            # Recortando o raster por Município
            for i in range(len(lim_buf)):
                try:
                    geom = []
                    coord = shapely.geometry.mapping(lim_buf.iloc[i].geometry)
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
                    with rasterio.open(f'{output}_{names[i]}.tif', 'w', **out_meta) as dest:
                        dest.write(out_image)
                except Exception as e:
                    print(f"  Erro ao recortar município {names[i]}: {str(e)}")
        
        # Buscar imagens recortadas
        print("\nBuscando imagens recortadas para reclassificação...")
        imagens = glob.glob(temp_path + '**/*.tif')
        print(f"Encontradas {len(imagens)} imagens recortadas")
        
        # Reclassificação das imagens
        print("\nIniciando reclassificação das imagens...")
        for i, arquivo in enumerate(imagens, 1):
            if ".tif" in arquivo and ".lock" not in arquivo and ".xml" not in arquivo:
                print(f"[{i}/{len(imagens)}] Reclassificando: {os.path.basename(arquivo)}")
                try:
                    driver = gdal.GetDriverByName('GTiff')
                    input = gdal.Open(arquivo)
                    band = input.GetRasterBand(1)
                    band1 = band.ReadAsArray()
                    lista = band1.copy()
                    
                    # Reclassificação conforme critérios
                    lista[np.where(np.logical_or(lista == 0, lista == 27))] = 0  # Sem dados
                    lista[np.where(lista == 15)] = 1  # Pastagem natural ou plantadas
                    lista[np.where(np.logical_or(lista == 18, lista == 19))] = 2  # Agricultura
                    lista[np.where(np.logical_or(lista == 20, lista == 36))] = 2  # Agricultura
                    lista[np.where(np.logical_or(lista == 39, lista == 40))] = 2  # Agricultura
                    lista[np.where(np.logical_or(lista == 41, lista == 46))] = 2  # Agricultura
                    lista[np.where(np.logical_or(lista == 47, lista == 48))] = 2  # Agricultura
                    lista[np.where(lista == 62)] = 2  # Agricultura
                    lista[np.where(lista == 21)] = 3  # Agropecuário mosaico de agricultura e pastagem
                    lista[np.where(lista == 9)] = 4  # Silvicultura
                    lista[np.where(np.logical_or(lista == 23, lista == 25))] = 5  # Áreas não vegetadas
                    lista[np.where(lista == 29)] = 5  # Áreas não vegetadas
                    lista[np.where(np.logical_or(lista == 3, lista == 4))] = 6  # Vegetação natural florestal
                    lista[np.where(np.logical_or(lista == 5, lista == 49))] = 6  # Vegetação natural florestal
                    lista[np.where(np.logical_or(lista == 11, lista == 12))] = 7  # Vegetação natural não florestal
                    lista[np.where(np.logical_or(lista == 13, lista == 32))] = 7  # Vegetação natural não florestal
                    lista[np.where(lista == 50)] = 7  # Vegetação natural não florestal
                    lista[np.where(np.logical_or(lista == 24, lista == 30))] = 8  # Área urbana ou mineração
                    lista[np.where(np.logical_or(lista == 31, lista == 33))] = 9  # Água e aquicultura
                    
                    # Definindo o caminho de saída
                    nome_arquivo = os.path.basename(arquivo)
                    nome_arquivo = nome_arquivo.replace("brasil_coverage", "Usos_ABC")
                    rast_reclass = os.path.join(temp_path, nome_arquivo)
                    
                    output = driver.Create(rast_reclass, input.RasterXSize, input.RasterYSize, 1)
                    output.GetRasterBand(1).WriteArray(lista)
                    proj = input.GetProjection()
                    georef = input.GetGeoTransform()
                    output.SetProjection(proj)
                    output.SetGeoTransform(georef)
                    output.FlushCache()
                except Exception as e:
                    print(f"  Erro ao reclassificar {os.path.basename(arquivo)}: {str(e)}")
        
        # Buscar rasters Usos ABC
        print("\nBuscando rasters reclassificados...")
        rasters = glob.glob(temp_path + '**/Usos_ABC*.tif')
        print(f"Encontrados {len(rasters)} rasters reclassificados")
        
        # Convertendo Raster para Shapefile
        print("\nIniciando conversão de raster para shapefile...")
        for i, raster in enumerate(rasters, 1):
            if ".tif" in raster and ".lock" not in raster and ".xml" not in raster:
                print(f"[{i}/{len(rasters)}] Convertendo: {os.path.basename(raster)}")
                try:
                    caminho = os.path.join(temp_path, raster)
                    driver = gdal.GetDriverByName('GTiff')
                    input = gdal.Open(raster)
                    band = input.GetRasterBand(1)
                    band1 = band.ReadAsArray()
                    proj = input.GetProjection()
                    shp_proj = osr.SpatialReference()
                    shp_proj.ImportFromWkt(proj)
                    
                    output = raster.replace('.tif', '_temp1.shp')
                    call_drive = ogr.GetDriverByName('ESRI Shapefile')
                    create_shp = call_drive.CreateDataSource(output)
                    shp_layer = create_shp.CreateLayer('Usos_ABC', srs=shp_proj)
                    
                    new_field = ogr.FieldDefn(str('CD_USO'), ogr.OFTInteger)
                    shp_layer.CreateField(new_field)
                    
                    gdal.Polygonize(band, None, shp_layer, 0, [], callback=None)
                    create_shp.Destroy()
                    
                    # Dissolver por CD_USO
                    geodf = gpd.read_file(output)
                    dissolve = geodf.dissolve(by='CD_USO')
                    out_dis = raster.replace('.tif', '_temp2.shp')
                    dissolve.to_file(driver='ESRI Shapefile', filename=out_dis)
                except Exception as e:
                    print(f"  Erro ao converter {os.path.basename(raster)}: {str(e)}")
        
        # Cortar por Município
        print("\nRecortando shapefiles por município...")
        # Agrupar por Município
        agrupado = lim.groupby('CD_MUN')
        
        # Shapefiles que serão recortados
        shapes = glob.glob(temp_path + '**/*temp2.shp')
        print(f"Encontrados {len(shapes)} shapefiles para recorte")
        
        for i, shape in enumerate(shapes, 1):
            print(f"[{i}/{len(shapes)}] Processando: {os.path.basename(shape)}")
            
            for key, values in agrupado:
                if key in shape:
                    try:
                        usos = gpd.read_file(shape)
                        usos = usos.to_crs(epsg=4326)
                        nome_arq = os.path.basename(shape).replace("_temp2.shp", ".shp")
                        output = os.path.join(out_path, nome_arq)
                        
                        mun = lim[lim["CD_MUN"] == f"{key}"]
                        geodf_clip = gpd.clip(usos, mun)
                        geodf_clip.to_file(driver='ESRI Shapefile', filename=output)
                    except Exception as e:
                        print(f"  Erro ao recortar {key} de {os.path.basename(shape)}: {str(e)}")
        
        # Movendo os arquivos para as pastas dos respectivos anos
        print("\nOrganizando arquivos por ano...")
        lista_arquivos = os.listdir(out_path)
        
        for arquivo in lista_arquivos:
            if 'Usos_ABC' in arquivo and os.path.isfile(os.path.join(out_path, arquivo)):
                try:
                    caminho_arquivo = os.path.join(out_path, arquivo)
                    # Extrair o ano do nome do arquivo
                    partes = os.path.basename(arquivo).split("_")
                    if len(partes) >= 3:
                        ano = partes[2]
                        if ano in anos:
                            pasta_destino = os.path.join(out_path, ano)
                            if not os.path.exists(pasta_destino):
                                os.makedirs(pasta_destino, exist_ok=True)
                            
                            destino = os.path.join(pasta_destino, arquivo)
                            shutil.move(caminho_arquivo, destino)
                            print(f"  Movido: {arquivo} → {ano}/")
                except Exception as e:
                    print(f"  Erro ao mover {arquivo}: {str(e)}")
        
        print("\nProcessamento de Usos ABC concluído com sucesso!")
        return 0
        
    except Exception as e:
        print(f"\nERRO: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 