# Script para integração do Uso ABC 2021 com as bases: Declividade, Edafo, TI, UCPI e Amazônia Legal
# Módulos necessários
import os
import glob
import geopandas as gpd
# Definir diretório principal
dir_path = r"D:\10_MILLENIUM\04_DADOS\02_DADOS_INTEGRACAO_INTERFACE\INTERSECTS"
# Definir pasta com os arquivos de Edafo por município
edafo_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Terras_Indigenas\Terras_Indigenas_Municipios"
# Definir pasta com os arquivos do CAR
car_path = r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\CAR_DF_SE_2023\CAR_municipios"
# Criar pasta para armazenar arquivos temporários
temp_path = os.path.join(dir_path, 'Temporarios')
os.makedirs(temp_path, exist_ok=True)
# Listar anos para integração
anos = ['2008', '2021']
# Listar Municipios
municipios = []
imoveis = glob.glob(car_path + '**/*.shp')
for imovel in imoveis:
    municipio = os.path.basename(imovel).replace('Imoveis_', '').replace('.shp', '')
    municipios.append(municipio)
# Interseção 2: Usos ABC + Declividade + Edafo
# Criar pasta para armazenar o resultado da integração
# Caminho dos vetores dos usos
for ano in anos:
    usos = glob.glob(temp_path + fr'**/*{ano}*UCPI.shp')
    edafo = glob.glob(edafo_path + '**/*.shp')
    caminho_usos = []
    caminho_edafo = []
    for arquivo in usos:
        caminho = os.path.join(temp_path,arquivo)
        caminho_usos.append(caminho)
    for arquivo in edafo:
        caminho = os.path.join(edafo_path,arquivo)
        caminho_edafo.append(caminho)
    vetores = caminho_usos + caminho_edafo
    for municipio in municipios:
        for vetor in vetores:
            if municipio in vetor and 'Usos' in vetor:
                nome_arq = os.path.basename(vetor)
                uso = gpd.read_file(vetor)
            if municipio in vetor and 'TI' in vetor:
                edafo = gpd.read_file(vetor)
        base_car = gpd.overlay(uso, edafo, how='intersection', keep_geom_type=True)
        base_car.to_file(driver = 'ESRI Shapefile', filename = (rf'{temp_path}\{nome_arq}'))