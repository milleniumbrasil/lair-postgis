# Script para recortar a base de Amazônia Legal por Estado e por Municípios
# Módulos necessários
from pyogrio import read_dataframe
import geopandas as gpd
import pandas as pd
import os
import glob
import numpy as np
# Definir diretório principal
dirpath = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Amazonia_Legal"
# Criar pasta para armazenar a base de Amazônia Legal recortada por estado
uf_path = os.path.join(dirpath, 'Amz_Legal_Estados')
os.makedirs(uf_path, exist_ok=True)
# Criar pasta para armazenar a base de Amazônia Legal recortada por municípios
mun_path = os.path.join(dirpath, 'Amz_Legal_Municipios')
os.makedirs(mun_path, exist_ok=True)
# Ler o arquivo original de Amazônia Legal
base = read_dataframe(r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Amazonia_Legal\Original\BR_Amazonia_Legal_2021.shp")
base = base.to_crs(epsg=4326)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR)
lim = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Limites_territoriais_IBGE\Limites_Territoriais\BR_UF_Meso_Micro_Mun_2022.shp")
# Cortar por estado
# Agrupar por estado
agrupado = lim.groupby('SIGLA_UF')
for key,values in agrupado:
    output = uf_path + f'\Amz_Legal_2021_{key}.shp'
    uf = lim[lim["SIGLA_UF"] == f"{key}"]
    geodf_clip = gpd.clip(base, uf, keep_geom_type=True)
    geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
# Lista dos estados
estados = list(np.unique(lim['SIGLA_UF']))
# Cortar por município
for estado in estados:
    shapes = glob.glob(uf_path + f'**/*{estado}.shp')
    # Selecionar GeoDataFrame por estado
    select = lim[lim['SIGLA_UF'] == f'{estado}']
    # Agrupar por município
    agrupado = select.groupby('CD_MUN')
    for shape in shapes:
        for key,values in agrupado:
            amz = read_dataframe(shape)
            amz = amz.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape)
            nome_arq = nome_arq.replace('.shp', f'_{key}.shp')
            output = mun_path + f"\{nome_arq}"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(amz, mun, keep_geom_type=True)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))