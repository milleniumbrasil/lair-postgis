# Script para adequar a base de Terras Indígenas
# Módulos necessários
from pyogrio import read_dataframe
import geopandas as gpd
import pandas as pd
import os
import glob
import numpy as np
# Definir diretório principal
dirpath = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Terras_Indigenas"
# Criar pasta para armazenar a base de Terra Indígena recortada por estado
uf_path = os.path.join(dirpath, 'Terras_Indigenas_Estados')
os.makedirs(uf_path, exist_ok=True)
# Criar pasta para armazenar a base de Terra Indígena recortada por municípios
mun_path = os.path.join(dirpath, 'Terras_Indigenas_Municipios')
os.makedirs(mun_path, exist_ok=True)
# Ler o arquivo original de Terra Indígena (tis_poligonais.shp)
base = read_dataframe(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\tis_poligonais\tis_poligonais.shp")
base = base.to_crs(epsg=4326)
# Ler limite do Brasil
brasil = read_dataframe(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\BR_Pais_2022.shp")
brasil = brasil.to_crs(epsg=4326)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR)
lim = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Limites_territoriais_IBGE\Limites_Territoriais\BR_UF_Meso_Micro_Mun_2022.shp")
# Adicionar coluna TERRIND_C
base['CD_TERRIND'] = '1'
# Listar as colunas do dataframe
colunas = list(base.columns)
colunas = [coluna for coluna in colunas if 'CD_TERRIND' not in coluna and 'terrai_cod' not in coluna and 'geometry' not in coluna]
# Excluindo as colunas desnecessárias
base = base.drop(colunas, axis = 1)
# Fazer a diferença entre a base de terras indígenas e o limite do Brasil
erase = brasil.overlay(base, how='difference', keep_geom_type=True)
# Transformar para Single Part
single = erase.explode(ignore_index=True)
# Merge da terra indígena com o erase
merge = pd.concat([base, single]).pipe(gpd.GeoDataFrame)
# Excluindo colunas desnecessárias
merge = merge.drop(['NM_PAIS', 'AREA_KM2'], axis = 1)
# Preencher os valores nulos por 0
merge.update(merge['CD_TERRIND'].fillna('0'))
# Cortar por estado
# Agrupar por estado
agrupado = lim.groupby('SIGLA_UF')
for key,values in agrupado:
    output = uf_path + f'\TI_2022_{key}.shp'
    mun = lim[lim["SIGLA_UF"] == f"{key}"]
    geodf_clip = gpd.clip(merge, mun)
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
            ti = read_dataframe(shape)
            ti = ti.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape)
            nome_arq = nome_arq.replace('.shp', f'_{key}.shp')
            output = mun_path + f"\{nome_arq}"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(ti, mun)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
