# Script para tratar base do Mapbiomas para gerar o Usos ABC por ano e por município
# Módulos necessários
import os
import glob
import rasterio
from rasterio.mask import mask
import shapely
import geopandas as gpd
from osgeo import ogr, osr, gdal
import numpy as np
import shutil
import time
# Definir diretório principal
dirpath = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Usos_ABC"
# Definir as pastas com imagens originais do Mapbiomas
originais_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Usos_ABC\Originais"
# Criar pasta para armazenar arquivos temporários
temp_path = os.path.join(dirpath, 'Temporarios')
os.makedirs(temp_path, exist_ok=True)
# Criar pasta para armazenar os arquivos finais de Usos ABC por município
out_path = os.path.join(dirpath, 'Usos_ABC_Municipios')
os.makedirs(out_path, exist_ok=True)
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR - Buffer de 150 metros)
lim_buf = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\BR_Municipios_2022_SE_DF_buf.shp")
# Lendo shapefile que será usado como máscara para recorte (Limites territoriais do BR)
lim = gpd.read_file(r"D:\10_MILLENIUM\04_DADOS\Entradas_Shapes\Shapes\BR_Municipios_2022_SE_DF.shp")
# Códigos dos municípios
names = [x for x in lim_buf['CD_MUN']]
# Imagens a serem recortadas
imagens = glob.glob(originais_path + '**/*.tif')
# Recortando os rasters do Mapbiomas por município
for raster in imagens:
    # Lendo o raster
    ras_data = rasterio.open(raster)
    # Definindo o caminho de saída do raster recortado
    nome_arquivo = os.path.basename(raster)
    nome_arquivo = nome_arquivo.replace('.tif', '')
    output = os.path.join(temp_path, nome_arquivo)
    # Recortando o raster por microrregião
    for i in range(len(lim_buf)):
        geom = []
        coord = shapely.geometry.mapping(lim_buf)["features"][i]["geometry"]
        geom.append(coord)
        with rasterio.open(raster) as src:
            out_image, out_transform = rasterio.mask.mask(src,geom,crop=True)
            out_meta = src.meta
        out_meta.update({'driver':'GTiff',
                         'height':out_image.shape[1],
                         'width':out_image.shape[2],
                         'transform':out_transform})
        # Salvando os rasters recortados
        with rasterio.open(f'{output}_{names[i]}.tif','w',**out_meta)as dest: dest.write(out_image)
# Buscar imagens recortadas
imagens = glob.glob(temp_path + '**/*.tif')
# Criar uma lista vazia para armazenar o DataSetReads das imagens a serem reclassificadas
imagens_rcls = []
# Iniciar loop para abrir as imagens a serem reclassificadas
for arquivo in imagens:
    if ".tif" in arquivo and ".lock" not in arquivo and ".xml" not in arquivo:
        #print(arquivo)
        caminho_arquivo=os.path.join(temp_path,arquivo)
        #print(caminho_arquivo)
        driver = gdal.GetDriverByName('GTiff')
        input = gdal.Open(caminho_arquivo)
        band = input.GetRasterBand(1)
        band1 = band.ReadAsArray()
        lista = band1.copy()
        lista[np.where(np.logical_or(lista == 0, lista == 27))] = 0 # Sem dados
        lista[np.where(lista == 15)] = 1 # Pastagem natural ou plantadas
        lista[np.where(np.logical_or(lista == 18, lista == 19))] = 2 # Agricultura
        lista[np.where(np.logical_or(lista == 20, lista == 36))] = 2 # Agricultura
        lista[np.where(np.logical_or(lista == 39, lista == 40))] = 2 # Agricultura
        lista[np.where(np.logical_or(lista == 41, lista == 46))] = 2 # Agricultura
        lista[np.where(np.logical_or(lista == 47, lista == 48))] = 2 # Agricultura
        lista[np.where(lista == 62)] = 2 # Agricultura
        lista[np.where(lista == 21)] = 3 # Agropecuário mosaico de agricultura e pastagem
        lista[np.where(lista == 9)] = 4 # Silvicultura
        lista[np.where(np.logical_or(lista == 23,lista == 25))] = 5 # Áreas não vegetadas
        lista[np.where(lista == 29)] = 5 # Áreas não vegetadas
        lista[np.where(np.logical_or(lista == 3, lista == 4))] = 6 # Vegetação natural florestal
        lista[np.where(np.logical_or(lista == 5, lista == 49))] = 6 # Vegetação natural florestal
        lista[np.where(np.logical_or(lista == 11, lista == 12))] = 7 # Vegetação natural não florestal
        lista[np.where(np.logical_or(lista == 13, lista == 32))] = 7 # Vegetação natural não florestal
        lista[np.where(lista == 50)] = 7 # Vegetação natural não florestal
        lista[np.where(np.logical_or(lista == 24, lista == 30))] = 8 # Área de influência urbana - urbano ou mineração
        lista[np.where(np.logical_or(lista == 31, lista == 33))] = 9 # Água e aquicultura
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
# Buscar rasters Usos ABC
rasters = glob.glob(temp_path + '**/Usos_ABC*.tif')
# Convertendo Raster para Shapefile
for raster in rasters:
    if ".tif" in raster and ".lock" not in raster and ".xml" not in raster:
        caminho = os.path.join(temp_path, raster)
        driver = gdal.GetDriverByName('GTiff')
        input = gdal.Open(caminho)
        band = input.GetRasterBand(1)
        band1 = band.ReadAsArray()
        proj = input.GetProjection()
        shp_proj = osr.SpatialReference()
        shp_proj.ImportFromWkt(proj)
        output = caminho.replace('.tif', '_temp1.shp')
        call_drive = ogr.GetDriverByName('ESRI Shapefile')
        create_shp = call_drive.CreateDataSource(output)
        shp_layer = create_shp.CreateLayer('Usos_ABC', srs = shp_proj)
        new_field = ogr.FieldDefn(str('CD_USO'), ogr.OFTInteger)
        shp_layer.CreateField(new_field)
        gdal.Polygonize(band, None, shp_layer, 0, [], callback = None)
        create_shp.Destroy()
        raster = None
        geodf = gpd.read_file(output)
        dissolve = geodf.dissolve(by='CD_USO')
        out_dis = caminho.replace('.tif', '_temp2.shp')
        dissolve.to_file(driver = 'ESRI Shapefile', filename = out_dis)
# Cortar por município
# Agrupar por Município - cria um DataFrameGroupBy que é semelhante a um dicionário sendo possível iterar sob as feições
agrupado = lim.groupby('CD_MUN')
# Shapefiles que serão recortados
shapes = glob.glob(temp_path + '**/*temp2.shp')
for shape in shapes:
    for key,values in agrupado:
        if key in shape:
            usos = gpd.read_file(shape)
            usos = usos.to_crs(epsg=4326)
            nome_arq = os.path.basename(shape).replace("_temp2.shp", ".shp")
            output = out_path + f"\{nome_arq}"
            mun = lim[lim["CD_MUN"] == f"{key}"]
            geodf_clip = gpd.clip(usos, mun)
            geodf_clip.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))
# Excluir pasta de arquivos temporários
time.sleep(5)
shutil.rmtree(temp_path)