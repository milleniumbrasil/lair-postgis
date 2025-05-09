#!/usr/bin/env python3
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("notebook-executor")

# Lista de notebooks na ordem correta de execução
notebooks = [
    "01_Download_CAR_estados.ipynb",
    "02_UsosABC.ipynb",
    "03_Declividade.ipynb",
    "04_CorrecaoEdafo.ipynb",
    "05_AptdEdafo.ipynb",
    "06_TerraIndigena.ipynb",
    "07_AmazoniaLegal.ipynb",
    "08_FaixaFronteira.ipynb",
    # Adicione os demais notebooks conforme necessário
]

# Diretório de trabalho
work_dir = os.getcwd()

# Executar cada notebook
for notebook_name in notebooks:
    notebook_path = os.path.join(work_dir, notebook_name)
    
    # Verificar se o notebook existe
    if not os.path.exists(notebook_path):
        logger.warning(f"Notebook {notebook_name} não encontrado, pulando...")
        continue
    
    logger.info(f"Iniciando execução do notebook: {notebook_name}")
    
    try:
        # Carregar o notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        # Criar o executor com timeout (3600 segundos = 1 hora)
        executor = ExecutePreprocessor(timeout=3600, kernel_name='python3')
        
        # Executar o notebook
        executor.preprocess(notebook, {'metadata': {'path': work_dir}})
        
        # Salvar o notebook com as saídas
        output_path = os.path.join(work_dir, f"executado_{notebook_name}")
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        
        logger.info(f"Notebook {notebook_name} executado com sucesso!")
    
    except Exception as e:
        logger.error(f"Erro ao executar o notebook {notebook_name}: {str(e)}")
        # Continuar com os demais notebooks mesmo em caso de erro

logger.info("Processo de execução de notebooks concluído!") 