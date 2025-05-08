import os
import json
import glob
import re

def substituir_input_por_env(notebook_path):
    """
    Substitui chamadas de input() por leituras de variáveis de ambiente em notebooks.
    """
    print(f"Processando: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    alterado = False
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            
            # Verificar se há qualquer chamada de input()
            if isinstance(source, list):
                source = ''.join(source)
            
            if 'input(' in source:
                print(f"  - Encontrado input() em célula")
                
                # Diferentes padrões de substituição baseados no conteúdo
                if "Diretório principal" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "dirpath = os.getenv('INPUT_PATH', '/app/input')\n"
                    ]
                elif "Diretório do CAR" in source or "CAR:" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "car_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'CAR')\n"
                    ]
                elif "Municípios:" in source or "Shapefile de Municípios" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "mun_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Municipios', 'BR_Municipios_2021.shp')\n"
                    ]
                elif "Caminho Faixa de Fronteira" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "faixa = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'FaixaFronteira', 'Faixa_Fronteira_2021.shp')\n"
                    ]
                elif "Diretório dos Usos ABC por município" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "uso_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Usos_ABC_Municipios')\n"
                    ]
                elif "Diretório da Declividade por município" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "decl_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Decliv_UF_Municipios')\n"
                    ]
                elif "Diretório da Aptidão do Solo por município" in source or "Aptidão Edáfica" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "edafo_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Aptd_Edafo_Municipios')\n"
                    ]
                elif "Diretório da Terra Indígena por município" in source or "Caminho Terra Indígena" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "ti_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Terras_Indigenas_Municipios')\n"
                    ]
                elif "Diretório de UCPI por município" in source or "Caminho UCPI" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "ucpi_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'UCPI_Municipios')\n"
                    ]
                elif "Diretório de Amazônia Legal por município" in source or "Caminho Amazônia Legal" in source:
                    novo_source = [
                        "# 🚨 Substituído automaticamente\n",
                        "import os\n",
                        "# Original: " + source.replace('\n', '\n# ') + "\n",
                        "amz_path = os.path.join(os.getenv('INPUT_PATH', '/app/input'), 'Amz_Legal_Municipios')\n"
                    ]
                else:
                    # Caso genérico para outros inputs não identificados
                    input_name = re.search(r'(\w+)\s*=\s*input\(', source)
                    if input_name:
                        var_name = input_name.group(1)
                        novo_source = [
                            "# 🚨 Substituído automaticamente\n",
                            "import os\n",
                            "# Original: " + source.replace('\n', '\n# ') + "\n",
                            f"{var_name} = os.path.join(os.getenv('INPUT_PATH', '/app/input'), '{var_name}')\n"
                        ]
                    else:
                        # Se não conseguir identificar o nome da variável
                        novo_source = [
                            "# 🚨 Substituído automaticamente\n",
                            "import os\n",
                            "# Original: " + source.replace('\n', '\n# ') + "\n",
                            "caminho = os.getenv('INPUT_PATH', '/app/input')\n"
                        ]
                
                # Substituir o conteúdo da célula
                cell['source'] = novo_source
                alterado = True
    
    if alterado:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
        print(f"✅ Notebook atualizado: {notebook_path}")
        return True
    else:
        print(f"⏩ Nenhuma alteração necessária em: {notebook_path}")
        return False

def main():
    # Diretório dos notebooks
    notebooks_dir = "."
    
    # Listar todos os notebooks
    notebooks = glob.glob(os.path.join(notebooks_dir, "*.ipynb"))
    
    notebooks_alterados = 0
    for notebook in notebooks:
        if not os.path.basename(notebook).startswith("output"):
            if substituir_input_por_env(notebook):
                notebooks_alterados += 1
    
    print(f"\n🎉 Processo concluído! {notebooks_alterados} notebooks foram atualizados.")

if __name__ == "__main__":
    main() 