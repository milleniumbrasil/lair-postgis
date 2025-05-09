#!/usr/bin/env python3
import json
import os

# Caminho para o notebook
notebook_path = "notebooks/05_AptdEdafo.ipynb"

# Carregar o notebook original
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Percorrer as células para identificar os caminhos e adicionar variáveis de ambiente
for i, cell in enumerate(notebook["cells"]):
    source = cell.get("source", "")
    
    # Se for uma célula de código
    if cell["cell_type"] == "code":
        joined_source = "".join(source) if isinstance(source, list) else source
        
        # Substituir caminhos por variáveis de ambiente
        if "dirpath =" in joined_source and "INPUT_PATH" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir diretório principal\n",
                "dirpath = os.getenv('INPUT_PATH', '/home/jovyan/data/input')\n"
            ]
        
        if "originais_path =" in joined_source and "INPUT_PATH" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir o caminho da pasta com os arquivos corrigidos de Aptidão Solo\n",
                "originais_path = os.path.join(os.getenv('INPUT_PATH', '/home/jovyan/data/input'), os.getenv('APTIDAO_CORRIGIDA_PATH', 'Aptidao_Solo_Corrigida'))\n"
            ]
        
        if "car_path =" in joined_source and "INPUT_PATH" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir pasta com os arquivos do CAR\n",
                "car_path = os.path.join(os.getenv('INPUT_PATH', '/home/jovyan/data/input'), os.getenv('CAR_FOLDER', 'CAR'))\n"
            ]
        
        if "mun_path =" in joined_source and "INPUT_PATH" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho do shapefile que será usado como máscara para recorte (Municípios do BR - sem Buffer)\n",
                "mun_path = os.path.join(os.getenv('INPUT_PATH', '/home/jovyan/data/input'), os.getenv('MUNICIPIOS_PATH', 'Municipios'), os.getenv('MUNICIPIOS_FILE', 'BR_Municipios_2021.shp'))\n"
            ]
        
        # Parametrizar os diretórios de saída
        if "out_path = os.path.join(dirpath, 'Aptd_Edafo_Municipios')" in joined_source:
            partes = joined_source.split('\n')
            novos_partes = []
            for parte in partes:
                if "out_path = os.path.join(dirpath, 'Aptd_Edafo_Municipios')" in parte:
                    novos_partes.append("out_path = os.path.join(dirpath, os.getenv('APTIDAO_MUN_OUTPUT', 'Aptd_Edafo_Municipios'))")
                elif "lim = gpd.read_file(limites)" in parte:
                    novos_partes.append("lim = gpd.read_file(mun_path)")
                else:
                    novos_partes.append(parte)
            
            notebook["cells"][i]["source"] = novos_partes
        
        # Parametrizar o diretório de saída final
        if "final_path = os.path.join(dirpath, 'Aptd_Edafo_Municipios_CAR')" in joined_source:
            partes = joined_source.split('\n')
            novos_partes = []
            for parte in partes:
                if "final_path = os.path.join(dirpath, 'Aptd_Edafo_Municipios_CAR')" in parte:
                    novos_partes.append("final_path = os.path.join(dirpath, os.getenv('APTIDAO_CAR_OUTPUT', 'Aptd_Edafo_Municipios_CAR'))")
                else:
                    novos_partes.append(parte)
            
            notebook["cells"][i]["source"] = novos_partes

# Salvar o notebook modificado
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print(f"Notebook atualizado: {notebook_path}") 