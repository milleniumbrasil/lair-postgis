#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para subir os dados para tabelas no PostgreSQL

Projeto: Sistema de Apoio à Caracterização de Imóveis Rurais  
Embrapa/2023
"""

import os
import glob
import sys
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine
from geoalchemy2 import Geometry, WKTElement

def verificar_dependencias():
    """Verifica se todas as dependências necessárias estão instaladas"""
    try:
        import pandas
        import geopandas
        import sqlalchemy
        from geoalchemy2 import Geometry, WKTElement
        return True
    except ImportError as e:
        print(f"ERRO: Dependência não encontrada: {str(e)}")
        print("\nInstale as dependências com pip:")
        print("pip install pandas geopandas sqlalchemy geoalchemy2 psycopg2-binary")
        return False

def main():
    """Função principal que exporta os dados para PostgreSQL"""
    # Verificar dependências primeiro
    if not verificar_dependencias():
        return 1
    
    print("\n" + "="*80)
    print("Exportação de dados para PostgreSQL")
    print("="*80 + "\n")
    
    try:
        # Definir aos parâmetros do banco de dados
        host = input("Host do PostgreSQL (padrão: localhost:5432): ") or "localhost:5432"
        database = input("Nome do banco de dados: ")
        user = input("Usuário: ")
        password = input("Senha: ")
        
        # Caminho da base de dados
        base_path = input("Caminho da pasta com shapefiles: ")
        
        # Definir qual o schema e table de acordo com a base de dados
        schema = input("Nome do schema (ex: Usos_ABC): ")
        table = input("Nome da tabela (ex: 2021): ")
        
        # Validar se os parâmetros foram fornecidos
        if not all([database, user, password, base_path, schema, table]):
            print("ERRO: Todos os parâmetros são obrigatórios!")
            return 1
        
        # Verificar se o diretório existe
        if not os.path.exists(base_path):
            print(f"ERRO: O diretório {base_path} não existe!")
            return 1
        
        # Conexão com o banco de dados
        print(f"\nConectando ao banco de dados PostgreSQL em {host}...")
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        try:
            engine = create_engine(connection_string)
            # Testar conexão
            conn = engine.connect()
            conn.close()
            print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"ERRO ao conectar ao banco de dados: {str(e)}")
            return 1
        
        # Criar schema se não existir
        try:
            engine.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
            print(f"Schema '{schema}' verificado/criado com sucesso.")
        except Exception as e:
            print(f"ERRO ao criar schema: {str(e)}")
            return 1
        
        # Lendo os shapefiles e exportando para o PostgreSQL
        print(f"\nProcessando shapefiles da pasta: {base_path}")
        shapefiles = glob.glob(os.path.join(base_path, "**/*.shp"), recursive=True)
        
        if not shapefiles:
            print(f"ERRO: Nenhum shapefile encontrado em {base_path}")
            return 1
        
        print(f"Encontrados {len(shapefiles)} shapefiles.")
        
        total_registros = 0
        for i, shape in enumerate(shapefiles, 1):
            print(f"[{i}/{len(shapefiles)}] Processando: {os.path.basename(shape)}")
            try:
                # Ler o shapefile
                gdf = gpd.read_file(shape)
                
                # Converter para EPSG:4326 (WGS84)
                gdf = gdf.to_crs(epsg=4326)
                
                # Explodir geometrias multi-parte
                gdf = gdf.explode(ignore_index=True)
                
                # Converter nomes de colunas para minúsculas
                gdf.columns = [x.lower() for x in gdf.columns]
                
                # Converter geometria para WKTElement
                gdf['geom'] = gdf['geometry'].apply(lambda x: WKTElement(x.wkt, srid=4326))
                
                # Remover coluna de geometria original
                gdf.drop(['geometry'], axis=1, inplace=True)
                
                # Exportar para o PostgreSQL
                gdf.to_sql(
                    f'{table}', 
                    engine, 
                    schema=f'{schema}', 
                    if_exists='append', 
                    index=False, 
                    dtype={'geom': Geometry('POLYGON', srid=4326)}
                )
                
                num_registros = len(gdf)
                total_registros += num_registros
                print(f"  ✓ Exportados {num_registros} registros de {os.path.basename(shape)}")
                
            except Exception as e:
                print(f"  ✗ ERRO ao processar {os.path.basename(shape)}: {str(e)}")
        
        print(f"\nExportação concluída! Total de {total_registros} registros exportados para {schema}.{table}")
        
        # Criar índice espacial para melhorar desempenho das consultas
        try:
            index_name = f"idx_{schema}_{table}_geom"
            engine.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {schema}.{table} USING GIST (geom)")
            print(f"Índice espacial {index_name} criado com sucesso.")
        except Exception as e:
            print(f"AVISO: Não foi possível criar índice espacial: {str(e)}")
        
        print("\nProcesso de exportação para PostgreSQL concluído com sucesso!")
        return 0
        
    except Exception as e:
        print(f"\nERRO: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 