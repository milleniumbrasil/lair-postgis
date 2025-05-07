# Script para corrigir a base de Aptidão Solo por UF
# Módulos necessários
import os
import glob
import geopandas as gpd
from pyogrio import read_dataframe
import numpy as np
import pandas as pd
import time
# Definir diretório principal
dirpath = r"D:\01_MILLENIUM\Correcao_Edafo"
# Definir as pastas com a aptidão solo por UF
vetores_path = r"D:\01_MILLENIUM\Correcao_Edafo\Solo_e_Aptidao_Solo_BR_por_UF"
# Lendo shapefile de Limites territoriais do BR
lim = gpd.read_file(r"D:\01_MILLENIUM\Correcao_Edafo\BR_UF_Meso_Micro_Mun_2022.shp")
# Reprojetando o shapefile para WGS84
lim = lim.to_crs(epsg=4326)
# Criar pasta para armazenar Aptidão Solo corrigida
out_path = os.path.join(dirpath, 'Aptidao_Solo_Corrigida')
os.makedirs(out_path, exist_ok=True)
# Caminhos dos vetores de aptidão solo
vetores = glob.glob(vetores_path + f'**/*.shp')
# Agrupar por Estado para ser possível iterar sob as feições
agrupado = lim.groupby('SIGLA_UF')
for vetor in vetores:
    for key, values in agrupado:
        if key in vetor:
            aptidao = read_dataframe(vetor)
            output = out_path + f'\Aptd_Edafo_{key}_temp1.shp'
            estado = lim[lim['SIGLA_UF'] == f"{key}"]
            erase = estado.overlay(aptidao, how='difference', keep_geom_type=True)
            single = erase.explode(ignore_index=True)
            single.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
vetores_erase = glob.glob(out_path + f'**/*temp1.shp')
vetores_aptidao = glob.glob(vetores_path + f'**/*.shp')
caminho_erase = []
caminho_aptidao = []
for arquivo in vetores_erase:
    caminho = os.path.join(out_path,arquivo)
    caminho_erase.append(caminho)
for arquivo in vetores_aptidao:
    caminho = os.path.join(vetores_path,arquivo)
    caminho_aptidao.append(caminho)
vetores = caminho_erase + caminho_aptidao
geodf = pd.concat([
    read_dataframe(vetor)
    for vetor in vetores
]).pipe(gpd.GeoDataFrame)
for key, values in agrupado:
    estado = lim[lim['SIGLA_UF'] == f"{key}"]
    output = out_path + f'\Aptd_Edafo_{key}_temp2.shp'
    geodf_clip = gpd.clip(geodf, estado, keep_geom_type=True)
    geodf_clip.to_file(driver = 'ESRI Shapefile', filename = rf'{output}')
# Preenchendo os valores null com valores próximos
vetores_temp2 = glob.glob(out_path + f'**/*temp2.shp')
for arquivo in vetores_temp2:
    temp2 = read_dataframe(arquivo)
    nome_arq = os.path.basename(arquivo).replace('temp2.shp', 'temp3.shp')
    output = out_path + f'\{nome_arq}'
    null = temp2[temp2['APTD_EDAFO'].isna()]
    not_null = temp2[temp2['APTD_EDAFO'].notna()]
    gdfspatial  = null.sjoin_nearest(not_null, max_distance=5)
    gdfspatial.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
# Merge das feições com null preenchido e shape original de edafo
vetores_temp3 = glob.glob(out_path + f'**/*temp3.shp')
caminho_temp3 = []
for arquivo in vetores_temp3:
    caminho = os.path.join(out_path,arquivo)
    caminho_temp3.append(caminho)
vetores = caminho_temp3 + caminho_aptidao
geodf = pd.concat([
    read_dataframe(vetor)
    for vetor in vetores
]).pipe(gpd.GeoDataFrame)
for key, values in agrupado:
    estado = lim[lim['SIGLA_UF'] == f"{key}"]
    output = out_path + f'\Aptd_Edafo_{key}_temp4.shp'
    geodf_clip = gpd.clip(geodf, estado, keep_geom_type=True)
    geodf_clip.to_file(driver = 'ESRI Shapefile', filename = rf'{output}')
# Exportando apenas colunas necessárias
vetores_temp4 = glob.glob(out_path + f'**/*temp4.shp')
for vetor in vetores_temp4:
    temp4 = read_dataframe(vetor)
    colunas = list(temp4.columns)
    colunas = [coluna for coluna in colunas if 'EDA' not in coluna and 'LEG' not in coluna and 'geometry' not in coluna]
    temp4 = temp4.drop(colunas, axis = 1).pipe(gpd.GeoDataFrame)
    temp4['APTD_EDAFO'].fillna(temp4['APTD_EDA_1'], inplace=True)
    temp4['CD_EDAFO'].fillna(temp4['CD_EDAFO_r'], inplace=True)
    temp4['CD_EDAFO'].fillna(temp4['CD_EDAFO_l'], inplace=True)
    temp4['LEG_SOLO'].fillna(temp4['LEG_SOLO_r'], inplace=True)
    temp4['LEG_SOLO'].fillna(temp4['LEG_SOLO_l'], inplace=True)
    remover = ['APTD_EDA_1', 'CD_EDAFO_r', 'CD_EDAFO_l', 'LEG_SOLO_r', 'LEG_SOLO_l']
    temp4 = temp4.drop(remover, axis = 1).pipe(gpd.GeoDataFrame)
    nome = os.path.basename(vetor).replace('_temp4.shp', '.shp')
    output = out_path + f"\{nome}"
    temp4.to_file(driver = 'ESRI Shapefile', filename = rf'{output}')
# Remover os arquivos temporários da pasta
time.sleep(5)
def excluir_arquivos_temporarios(pasta):
    for nome_arquivo in os.listdir(pasta):
        if "temp" in nome_arquivo:
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
                print(f"Arquivo excluído: {caminho_arquivo}")
diretorio = out_path
excluir_arquivos_temporarios(diretorio)