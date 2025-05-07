# Script para integrar as bases de limites territoriais do Brasil segundo o IBGE
# Módulos necessários
import os
import glob
import geopandas as gpd
# Definir diretório principal
dir_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Limites_territoriais_IBGE"
# Definir pasta com os limites territoriais (UF, Mesorregiões, Microrregiões e Municípios)
lim_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Limites_territoriais_IBGE\Originais"
# Criar pasta para armazenar o resultado da integração
out_path = os.path.join(dir_path, 'Limites_Territoriais')
os.makedirs(out_path, exist_ok=True)
# Interseção 1: UF e Mesorregiões
shapes = glob.glob(lim_path + '**/*.shp')
for shape in shapes:
    if 'UF' in shape:
        uf = gpd.read_file(shape)
    if 'Meso' in shape:
        meso = gpd.read_file(shape)
inter = gpd.overlay(uf, meso, how='intersection', keep_geom_type=True)
inter.to_file(driver = 'ESRI Shapefile', filename = (rf'{out_path}\temp1.shp'))
# Interseção 2: UF, Mesorregiões e Microrregiões
shapes = glob.glob(out_path + '**/*.shp')
for shape in shapes:
    if 'temp1' in shape:
        temp1 = gpd.read_file(shape)
shapes2 = glob.glob(lim_path + '**/*.shp')
for shape in shapes2:
    if 'Micro' in shape:
        micro = gpd.read_file(shape)
inter = gpd.overlay(temp1, micro, how='intersection', keep_geom_type=True)
inter.to_file(driver = 'ESRI Shapefile', filename = (rf'{out_path}\temp2.shp'))
# Excluindo colunas com informações duplicadas
colunas = ['AREA_KM2_1', 'SIGLA_UF_2', 'AREA_KM2_2', 'SIGLA_UF', 'AREA_KM2']
inter = inter.drop(colunas, axis=1)
inter.to_file(driver = 'ESRI Shapefile', filename = (rf'{out_path}\temp2.shp'))
# Interseção 3: UF, Mesorregiões, Microrregiões e Municípios
shapes = glob.glob(out_path + '**/*.shp')
for shape in shapes:
    if 'temp2' in shape:
        temp2 = gpd.read_file(shape)
shapes2 = glob.glob(lim_path + '**/*.shp')
for shape in shapes2:
    if 'Muni' in shape:
        mun = gpd.read_file(shape)
inter = gpd.overlay(temp2, mun, how='intersection', keep_geom_type=True)
inter.to_file(driver = 'ESRI Shapefile', filename = (rf'{out_path}\BR_UF_Meso_Micro_Mun_2022.shp'))
# Excluindo e renomeando colunas com informações duplicadas
inter = inter.drop(['SIGLA_UF'], axis=1)
inter = inter.rename({'SIGLA_UF_1':'SIGLA_UF'}, axis = 1)
inter = inter.to_crs(epsg=4326)
inter.to_file(driver = 'ESRI Shapefile', filename = (rf'{out_path}\BR_UF_Meso_Micro_Mun_2022.shp'))
# Remover os arquivos temporários da pasta
def excluir_arquivos_temporarios(pasta):
    for nome_arquivo in os.listdir(pasta):
        if "temp1" in nome_arquivo or "temp2" in nome_arquivo:
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
                print(f"Arquivo excluído: {caminho_arquivo}")
diretorio = out_path
excluir_arquivos_temporarios(diretorio)