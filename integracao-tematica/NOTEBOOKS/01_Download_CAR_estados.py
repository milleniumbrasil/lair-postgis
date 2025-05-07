#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para download de dados do CAR (Cadastro Ambiental Rural) por estado
Convertido do notebook original para execução independente
"""

import os
import sys
import subprocess
import platform

def instalar_dependencias():
    """Instala as dependências necessárias para executar o script."""
    print("Instalando dependências...")
    
    # Instalar a biblioteca SICAR do GitHub
    subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/urbanogilson/SICAR"])
    
    # Instalar o Tesseract OCR dependendo do sistema operacional
    sistema = platform.system()
    if sistema == "Linux":
        print("Instalando Tesseract OCR (pode solicitar senha de administrador)...")
        try:
            subprocess.check_call(["sudo", "apt", "install", "tesseract-ocr", "-y"])
        except:
            print("Não foi possível instalar o Tesseract OCR automaticamente.")
            print("Por favor, instale manualmente o Tesseract OCR conforme documentação do seu sistema.")
    elif sistema == "Darwin":  # macOS
        print("No macOS, instale o Tesseract OCR usando Homebrew com o comando:")
        print("brew install tesseract")
    elif sistema == "Windows":
        print("No Windows, baixe e instale o Tesseract OCR a partir de:")
        print("https://github.com/UB-Mannheim/tesseract/wiki")
    
    print("Todas as dependências foram instaladas ou verificadas.")

def main():
    """Função principal que realiza o download dos dados do CAR por estado."""
    try:
        # Importação dos pacotes necessários
        from SICAR import Sicar
        import os
    except ImportError:
        print("Dependências não encontradas. Instalando...")
        instalar_dependencias()
        
        # Tentar importar novamente após a instalação
        try:
            from SICAR import Sicar
            import os
        except ImportError:
            print("Erro ao importar dependências mesmo após a instalação.")
            print("Por favor, verifique se todas as dependências foram instaladas corretamente.")
            return 1
    
    print("\n" + "="*80)
    print("Download de dados do CAR (Cadastro Ambiental Rural) por estado")
    print("="*80 + "\n")
    
    # Login para acessar o Sicar
    print("Configurando acesso ao SICAR...")
    # Aqui precisaria de um email válido para acesso ao SICAR
    email = input("Digite o email para acesso ao SICAR: ")
    car = Sicar(email=email)
    
    # Lista com estados de interesse para download
    states = ['AC','AM','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA',
              'MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF','RO','RR']
    
    # Caminho onde será armazenado os downloads
    caminho = input('Digite o caminho para armazenar os downloads do CAR: ')
    
    # Criar diretório se não existir
    if not os.path.exists(caminho):
        os.makedirs(caminho, exist_ok=True)
        print(f"Diretório criado: {caminho}")
    
    # Download dos estados de acordo com a lista
    print("\nIniciando download dos dados por estado...")
    for i, state in enumerate(states, 1):
        print(f"[{i}/{len(states)}] Baixando dados do estado: {state}")
        estado_path = os.path.join(caminho, state)
        
        # Criar diretório para o estado se não existir
        if not os.path.exists(estado_path):
            os.makedirs(estado_path, exist_ok=True)
        
        # Download do estado
        try:
            car.download_state(state=f'{state}', folder=estado_path, debug=False)
            print(f"✓ Download de {state} concluído")
        except Exception as e:
            print(f"✗ Erro ao baixar {state}: {str(e)}")
    
    print("\nProcesso de download concluído!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 