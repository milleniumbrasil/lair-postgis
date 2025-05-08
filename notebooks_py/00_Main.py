#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script principal para execução sequencial de todos os scripts de integração temática.
"""

import os
import sys
import subprocess
import time

def executar_script(script_path, descricao):
    """Executa um script Python e exibe mensagens de status."""
    print(f"\n{'='*80}")
    print(f"Executando: {descricao}")
    print(f"{'='*80}")
    
    start_time = time.time()
    try:
        resultado = subprocess.run([sys.executable, script_path], check=True)
        if resultado.returncode == 0:
            tempo_execucao = time.time() - start_time
            print(f"✓ {descricao} concluído com sucesso! (Tempo: {tempo_execucao:.2f}s)")
            return True
        else:
            print(f"✗ {descricao} falhou com código de erro {resultado.returncode}")
            return False
    except Exception as e:
        print(f"✗ Erro ao executar {descricao}: {str(e)}")
        return False

def main():
    """Função principal que executa todos os scripts em sequência."""
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Lista de scripts a serem executados em ordem
    scripts = [
        {"arquivo": "01_Download_CAR_estados.py", "descricao": "Download de dados CAR estados"},
        {"arquivo": "02_UsosABC.py", "descricao": "Usos ABC"},
        {"arquivo": "03_Declividade.py", "descricao": "Declividade"},
        {"arquivo": "04_CorrecaoEdafo.py", "descricao": "Correção Edafoclimática"},
        {"arquivo": "05_AptdEdafo.py", "descricao": "Aptidão Edafoclimática"},
        {"arquivo": "06_TerraIndigena.py", "descricao": "Terra Indígena"},
        {"arquivo": "07_AmazoniaLegal.py", "descricao": "Amazônia Legal"},
        {"arquivo": "08_FaixaFronteira.py", "descricao": "Faixa Fronteira"},
        {"arquivo": "09_UCPI.py", "descricao": "Unidades de Conservação de Proteção Integral"},
        {"arquivo": "10_IntegracoesCAR.py", "descricao": "Integrações CAR"},
        {"arquivo": "11_AdequarParaBancoDados.py", "descricao": "Adequar para Banco de Dados"},
        {"arquivo": "12_To_PostGis.py", "descricao": "Exportar para PostGIS"}
    ]
    
    print(f"\n{'='*80}")
    print("INTEGRAÇÃO TEMÁTICA - EXECUÇÃO DE SCRIPTS")
    print(f"{'='*80}")
    print(f"Total de scripts a executar: {len(scripts)}")
    
    sucessos = 0
    falhas = []
    
    # Executar cada script em sequência
    for i, script in enumerate(scripts, 1):
        caminho_script = os.path.join(pasta_atual, script["arquivo"])
        if os.path.exists(caminho_script):
            print(f"\nScript {i}/{len(scripts)}: {script['descricao']}")
            if executar_script(caminho_script, script["descricao"]):
                sucessos += 1
            else:
                falhas.append(script["descricao"])
        else:
            print(f"Arquivo não encontrado: {caminho_script}")
            falhas.append(script["descricao"])
    
    # Resumo da execução
    print(f"\n{'='*80}")
    print(f"RESUMO DA EXECUÇÃO:")
    print(f"{'='*80}")
    print(f"Total de scripts: {len(scripts)}")
    print(f"Executados com sucesso: {sucessos}")
    print(f"Falhas: {len(falhas)}")
    
    if falhas:
        print("\nScripts que falharam:")
        for falha in falhas:
            print(f"- {falha}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 