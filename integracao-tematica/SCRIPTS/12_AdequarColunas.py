# Script para adequar as colunas da base final de integração
# Módulos necessários
from pyogrio import read_dataframe
import geopandas as gpd
import pandas as pd
import os
import glob
import numpy as np
# # Definir diretório principal
# dirpath = r"D:\01_MILLENIUM\02_INTEGRACOES_CAR"
# Definir diretório com as integrações
base_path = r"D:\10_MILLENIUM\04_DADOS\01_DADOS_SANDRO\Declividade\Decliv_CAR_Municipios"
# # Criar pasta para armazenar a base final
# out_path = os.path.join(dirpath, 'Integracao_Propriedades')
# os.makedirs(out_path, exist_ok=True)
# Listar arquivos
shapes = glob.glob(base_path + f'**/*.shp')
for shape in shapes:
    base = read_dataframe(shape)
    colunas = list(base.columns)
    colunas = [coluna for coluna in colunas if 'COD_IMOVEL' not in coluna and 'NUM_AREA' not in coluna and 'COD_ESTADO' not in coluna
               and 'NOM_MUNICI' not in coluna and 'NUM_MODULO' not in coluna and 'TIPO_IMOVE' not in coluna
               and 'SITUACAO' not in coluna and 'CONDICAO_I' not in coluna and 'CD_DECLIV' not in coluna
               and 'geometry' not in coluna]
    base = base.drop(colunas, axis = 1)
    nome = os.path.basename(shape)
    output = base_path + f"\{nome}"
    base.to_file(driver = 'ESRI Shapefile', filename = (rf'{output}'))

