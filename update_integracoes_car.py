#!/usr/bin/env python3
import json
import os

# Caminho para o notebook
notebook_path = "notebooks/10_IntegracoesCAR.ipynb"

# Carregar o notebook original
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Percorrer as células para identificar os caminhos e adicionar variáveis de ambiente
for i, cell in enumerate(notebook["cells"]):
    source = cell.get("source", [])
    
    # Se for uma célula de código
    if cell["cell_type"] == "code":
        joined_source = "".join(source) if isinstance(source, list) else source
        
        # Modificar a célula que define a lista de anos
        if "# Listar anos de integração" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Listar anos de integração\n",
                "anos = os.getenv('INTEGRACAO_ANOS', '2008,2021').split(',')\n"
            ]
        
        # Identificar a célula com o código para pasta temporários
        elif "# Criar pasta para armazenar arquivos temporários" in joined_source:
            lines = joined_source.split('\n')
            new_source = []
            for line in lines:
                if "temp_path = os.path.join(dirpath, 'Temporarios')" in line:
                    new_source.append("temp_path = os.path.join(dirpath, os.getenv('INTEGRACAO_TEMP_FOLDER', 'Temporarios'))")
                else:
                    new_source.append(line)
            
            notebook["cells"][i]["source"] = new_source
        
        # Identificar a célula com o código para pasta potencial agropecuário
        elif "# Criar pasta para armazenar arquivos finais de Potencial Agropecuário" in joined_source:
            lines = joined_source.split('\n')
            new_source = []
            for line in lines:
                if "pot_path = os.path.join(dirpath, 'Potencial_Agropecuario')" in line:
                    new_source.append("pot_path = os.path.join(dirpath, os.getenv('INTEGRACAO_OUTPUT', 'Potencial_Agropecuario'))")
                else:
                    new_source.append(line)
            
            notebook["cells"][i]["source"] = new_source
        
        # Sinalizar o uso de pastas anteriormente parametrizadas
        elif "car_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'CAR')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir pasta com os arquivos do CAR - reutilizando variável CAR_FOLDER\n", 
                "car_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('CAR_FOLDER', 'CAR'))\n"
            ]
        
        elif "uso_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Usos_ABC_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: Usos_ABC_Municipios\n",
                "uso_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('INTEGRACAO_USO_PATH', 'Usos_ABC_Municipios'))\n"
            ]
        
        elif "decl_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Decliv_UF_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: Decliv_UF_Municipios - reutilizando variável DECLIV_OUTPUT\n",
                "decl_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('DECLIV_OUTPUT', 'Decliv_UF_Municipios'))\n"
            ]
        
        elif "edafo_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Aptd_Edafo_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: Aptd_Edafo_Municipios - reutilizando variável APTIDAO_MUN_OUTPUT\n",
                "edafo_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('APTIDAO_MUN_OUTPUT', 'Aptd_Edafo_Municipios'))\n"
            ]
        
        elif "ti_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Terras_Indigenas_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: Terras_Indigenas_Municipios - reutilizando variável TI_MUNICIPIOS_OUTPUT\n",
                "ti_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('TI_MUNICIPIOS_OUTPUT', 'Terras_Indigenas_Municipios'))\n"
            ]
        
        elif "ucpi_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'UCPI_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: UCPI_Municipios - reutilizando variável UCPI_MUNICIPIOS_OUTPUT\n",
                "ucpi_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('UCPI_MUNICIPIOS_OUTPUT', 'UCPI_Municipios'))\n"
            ]
        
        elif "amz_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Amz_Legal_Municipios')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho da pasta: Amz_Legal_Municipios - reutilizando variável AMZ_MUNICIPIOS_OUTPUT\n",
                "amz_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('AMZ_MUNICIPIOS_OUTPUT', 'Amz_Legal_Municipios'))\n"
            ]
        
        elif "mun_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Municipios', 'BR_Municipios_2021.shp')" in joined_source:
            notebook["cells"][i]["source"] = [
                "# Definir caminho do shapefile de Municípios - reutilizando variáveis MUNICIPIOS_PATH e MUNICIPIOS_FILE\n",
                "mun_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), os.getenv('MUNICIPIOS_PATH', 'Municipios'), os.getenv('MUNICIPIOS_FILE', 'BR_Municipios_2021.shp'))\n"
            ]

# Salvar o notebook modificado
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print(f"Notebook atualizado: {notebook_path}") 