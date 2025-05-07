# Script para recortar a base de Aptidão Solo por Municípios do BR
# Módulos necessários
import os
import glob
import geopandas as gpd
import numpy as np
# Definir diretório principal
dirpath = r"C:\Users\YouX\Desktop\EDAFICA_TO"
# Definir o caminho da pasta com os arquivos originais de Aptidão Solo
originais_path = r"C:\Users\YouX\Desktop\EDAFICA_TO\Aptidao_Solo_Corrigida"
# Criar pasta para armazenar os arquivos de Aptidão Solo recortados por município
out_path = os.path.join(dirpath, 'Aptd_Edafo_Municipios')
os.makedirs(out_path, exist_ok=True)
# Lendo shapefile de Limites territoriais do BR
lim = gpd.read_file(r"C:\Users\YouX\Desktop\EDAFICAS_FORA_TO\TO_Municipios_2022.shp")
# Reprojetando o shapefile para WGS84
lim = lim.to_crs(epsg=4326)
# Códigos dos municípios
names = [x for x in lim['CD_MUN']]
# Lista dos estados
estados = list(np.unique(lim['SIGLA_UF']))
# Cortar por município
for estado in estados:
    shapes = glob.glob(originais_path + f'**/*{estado}.shp')
    # Selecionar GeoDataFrame por estado
    select = lim[lim['SIGLA_UF'] == f'{estado}']
    # Agrupar por município para ser possível iterar sob as feições
    agrupado = select.groupby('CD_MUN')
    for shape in shapes:
        for key,values in agrupado:
            aptd = gpd.read_file(shape)
            aptd = aptd.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape).replace('.shp', '')
            output = out_path + f"\{nome_arq}_{key}.shp"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(aptd, mun, keep_geom_type=True)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))