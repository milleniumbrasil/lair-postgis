#!/usr/bin/env python3
import json
import os

# Caminho para o notebook original
notebook_path = "notebooks/01_Download_CAR_estados.ipynb"

# Carregar o notebook original
with open(notebook_path, "r") as f:
    notebook = json.load(f)

# Encontrar a célula onde está a instalação do SICAR
for i, cell in enumerate(notebook["cells"]):
    source = "".join(cell.get("source", []))
    if "!pip install git+" in source:
        # Modificar a célula para usar a variável de ambiente
        notebook["cells"][i]["source"] = [
            "# Instalação dos pacotes necessários\n",
            "sicar_repo = os.getenv(\"SICAR_REPO\", \"https://github.com/urbanogilson/SICAR\")\n",
            "print(f\"Instalando SICAR a partir de: {sicar_repo}\")\n",
            "!pip install git+{sicar_repo}\n",
            "!apt-get update && apt-get install -y tesseract-ocr"
        ]
        break

# Salvar o notebook modificado
with open(notebook_path, "w") as f:
    json.dump(notebook, f, indent=1)

print(f"Notebook atualizado: {notebook_path}") 