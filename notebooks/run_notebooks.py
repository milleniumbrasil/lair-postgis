import os
import glob
import subprocess
import sys

def executar_notebooks():
    """
    Executa os notebooks após substituir os inputs por variáveis de ambiente.
    """
    # Primeiro, substituir os inputs nos notebooks
    print("🔄 Substituindo chamadas de input() nos notebooks...")
    subprocess.run(["python", "patch_notebooks_inputs.py"], check=True)
    
    # Lista de notebooks para executar
    notebooks = [
        "02_UsosABC.ipynb",
        "03_Declividade.ipynb",
        "04_CorrecaoEdafo.ipynb",
        "05_AptdEdafo.ipynb",
        "06_TerraIndigena.ipynb",
        "07_AmazoniaLegal.ipynb",
        "08_FaixaFronteira.ipynb",
        "09_UCPI.ipynb",
        "10_IntegracoesCAR.ipynb",
        "11_AdequarParaBancoDados.ipynb",
        "12_To_PostGis.ipynb"
    ]
    
    # Criar diretório para saída
    output_dir = os.path.join(os.getcwd(), "notebooks", "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Verificar variáveis de ambiente
    input_path = os.getenv("INPUT_PATH", "/home/jovyan/data/input")
    output_path = os.getenv("OUTPUT_PATH", "/home/jovyan/data/output")
    
    print(f"📂 INPUT_PATH: {input_path}")
    print(f"📂 OUTPUT_PATH: {output_path}")
    
    # Verificar se os diretórios existem
    os.makedirs(input_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    
    # Executar cada notebook
    for notebook in notebooks:
        notebook_path = os.path.join(os.getcwd(), "notebooks", notebook)
        output_notebook = os.path.join(output_dir, notebook)
        
        if os.path.exists(notebook_path):
            print(f"📔 Executando {notebook}...")
            try:
                subprocess.run([
                    "papermill", 
                    notebook_path, 
                    output_notebook,
                    "--log-output"
                ], check=True)
                print(f"✅ {notebook} executado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao executar {notebook}: {e}")
        else:
            print(f"⚠️ Notebook não encontrado: {notebook_path}")
    
    print("🎉 Processamento concluído!")

if __name__ == "__main__":
    executar_notebooks() 