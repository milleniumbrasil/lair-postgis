# Script para recortar o shapefile de Unidades de Conservação de Proteção Integral por estado e por municípios
# Módulos necessários
from pyogrio import read_dataframe
import geopandas as gpd
import os
import glob
import numpy as np
# Definir diretório principal
dirpath = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Unidades_Conservacao"
# Criar pasta para armazenar a base de UCPI recortada por estado
uf_path = os.path.join(dirpath, 'UCPI_Estados')
os.makedirs(uf_path, exist_ok=True)
# Criar pasta para armazenar a base de UCPI recortada por municípios
mun_path = os.path.join(dirpath, 'UCPI_Municipios')
os.makedirs(mun_path, exist_ok=True)
# Ler o arquivo de UCPI
base = read_dataframe(r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Unidades_Conservacao\Original\UCS_Brasil_Preenchido_QGIS.shp")
base = base.to_crs(epsg=4326)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR)
lim = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Limites_territoriais_IBGE\Limites_Territoriais\BR_UF_Meso_Micro_Mun_2022.shp")
# Cortar por estado
# Agrupar por estado
agrupado = lim.groupby('SIGLA_UF')
for key,values in agrupado:
    output = uf_path + fr'\UCPI_{key}.shp'
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
            ucpi = read_dataframe(shape)
            ucpi = ucpi.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape)
            nome_arq = nome_arq.replace('.shp', fr'_{key}.shp')
            output = mun_path + f"\{nome_arq}"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(ucpi, mun, keep_geom_type=True)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))