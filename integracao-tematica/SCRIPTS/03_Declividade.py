# Script para recortar base de Declividade por Municípios do Brasil
# Módulos necessários
import os
import glob
import rasterio
from rasterio.mask import mask
import shapely
import geopandas as gpd
from pyogrio import read_dataframe
import numpy as np
from osgeo import ogr, osr, gdal
import time
import shutil
# Definir diretório principal
dirpath = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Declividade"
# Definir as pastas com as declividades originais
originais_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Declividade\Originais"
# Criar pasta para armazenar os vetores de Declividade por municipio
out_path = os.path.join(dirpath, 'Decliv_UF_Municipios')
os.makedirs(out_path, exist_ok=True)
# Criar pasta para armazenar arquivos temporários
temp_path = os.path.join(dirpath, 'Temporarios')
os.makedirs(temp_path, exist_ok=True)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR - Buffer de 150 metros)
lim_buf = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\BR_Municipios_2022_SE_DF_buf.shp")
# Reprojetando o shapefile para WGS84
lim_buf = lim_buf.to_crs(epsg=4326)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR)
lim = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\BR_Municipios_2022_SE_DF.shp")
# Reprojetando o shapefile para WGS84
lim = lim.to_crs(epsg=4326)
# Lista dos estados
estados = list(np.unique(lim['SIGLA_UF']))
# Recortando os rasters de declividade pelo buffer dos municípios
for estado in estados:
    rasters = glob.glob(originais_path + fr'**/{estado}.tif')
    # Selecionar GeoDataFrame por estado
    select = lim_buf[lim_buf['SIGLA_UF'] == f'{estado}']
    # Códigos dos municípios
    names = [x for x in select['CD_MUN']]
    for raster in rasters:
        # Lendo o raster
        ras_data = rasterio.open(raster)
        # Definindo o caminho de saída do raster recortado
        nome_arquivo = os.path.basename(raster)
        nome_arquivo = nome_arquivo.replace('.tif', '')
        output = os.path.join(temp_path, nome_arquivo)
        # Recortando o raster por município
        for i in range(len(select)):
            geom = []
            coord = shapely.geometry.mapping(select)["features"][i]["geometry"]
            geom.append(coord)
            with rasterio.open(raster) as src:
                out_image, out_transform = rasterio.mask.mask(src,geom,crop=True)
                out_meta = src.meta
            out_meta.update({'driver':'GTiff',
                            'height':out_image.shape[1],
                            'width':out_image.shape[2],
                            'transform':out_transform})
            # Salvando os rasters recortados
            with rasterio.open(f'{output}_{names[i]}_temp1.tif','w',**out_meta)as dest: dest.write(out_image)
# Buscar imagens recortadas
imagens = glob.glob(temp_path + '**/*temp1.tif')
# Convertendo Raster para Shapefile
for imagem in imagens:
    driver = gdal.GetDriverByName('GTiff')
    input = gdal.Open(imagem)
    band = input.GetRasterBand(1)
    band1 = band.ReadAsArray()
    proj = input.GetProjection()
    shp_proj = osr.SpatialReference()
    shp_proj.ImportFromWkt(proj)
    nome_arq = os.path.basename(imagem).replace('temp1.tif', 'temp2.shp')
    output = temp_path + f"\{nome_arq}"
    call_drive = ogr.GetDriverByName('ESRI Shapefile')
    create_shp = call_drive.CreateDataSource(output)
    shp_layer = create_shp.CreateLayer('Declividade', srs = shp_proj)
    new_field = ogr.FieldDefn(str('CD_DECLIV'), ogr.OFTInteger)
    shp_layer.CreateField(new_field)
    gdal.Polygonize(band, None, shp_layer, 0, [], callback = None)
    create_shp.Destroy()
    raster = None
# Dissolve
imagens = glob.glob(temp_path + '**/*temp2.shp')
for imagem in imagens:
    geodf = gpd.read_file(imagem)
    dissolve = geodf.dissolve(by='CD_DECLIV')
    nome_arq = os.path.basename(imagem).replace('temp2.shp', 'temp3.shp')
    output = temp_path + f"\{nome_arq}"
    dissolve.to_file(driver = 'ESRI Shapefile', filename = output)
# Cortar por município
# Agrupar por município
agrupado = lim.groupby('CD_MUN')
# Shapefiles que serão recortados
shapes = glob.glob(temp_path + '**/*temp3.shp')
for shape in shapes:
    for key,values in agrupado:
        if key in shape:
            decliv = gpd.read_file(shape)
            decliv = decliv.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape).replace("_temp3.shp", ".shp")
            output = out_path + f"\Decliv_{nome_arq}"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(decliv, mun)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
# Excluir pasta de arquivos temporários
time.sleep(5)
shutil.rmtree(temp_path)