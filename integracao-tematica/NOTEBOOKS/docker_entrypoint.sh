#!/bin/bash
set -e

# Definir caminhos padrão caso não estejam definidos
INPUT_DIR=${INPUT_DIR:-"/data/inputs"}
OUTPUT_DIR=${OUTPUT_DIR:-"/data/outputs"}
TEMP_DIR=${TEMP_DIR:-"/data/temp"}

# Criar diretórios se não existirem
mkdir -p $INPUT_DIR $OUTPUT_DIR $TEMP_DIR

# Configurar variáveis de ambiente PostgreSQL (apenas se utilizadas)
if [[ -n "${POSTGRES_HOST}" ]]; then
    export POSTGRES_HOST
    export POSTGRES_PORT=${POSTGRES_PORT:-"5432"}
    export POSTGRES_DB=${POSTGRES_DB:-"lair"}
    export POSTGRES_USER=${POSTGRES_USER:-"postgres"}
    export POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-"postgres"}
    
    echo "================================================================"
    echo "Configurações de banco de dados:"
    echo "----------------------------------------------------------------"
    echo "Banco de dados: $POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"
    echo "================================================================"
fi

# Exibir configurações
echo "================================================================"
echo "Configurações do ambiente:"
echo "----------------------------------------------------------------"
echo "Diretório de entrada: $INPUT_DIR"
echo "Diretório de saída: $OUTPUT_DIR"
echo "Diretório temporário: $TEMP_DIR"
echo "================================================================"

# Verificar se existe o script solicitado
if [ -f "$1" ]; then
    echo "Executando script: $1"
    echo "Data/hora de início: $(date)"
    echo "----------------------------------------------------------------"
    
    # Registrar hora de início
    start_time=$(date +%s)
    
    # Executar o script Python e capturar código de saída
    python "$@"
    exit_code=$?
    
    # Registrar hora de término
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    
    echo "----------------------------------------------------------------"
    echo "Data/hora de término: $(date)"
    echo "Duração: $((duration / 60)) minutos e $((duration % 60)) segundos"
    
    if [ $exit_code -eq 0 ]; then
        echo "Status: ✅ Execução concluída com sucesso"
    else
        echo "Status: ❌ Falha na execução (código $exit_code)"
    fi
    echo "================================================================"
    
    # Retornar o mesmo código de saída do script Python
    exit $exit_code
else
    # Se o primeiro argumento não for um script existente, 
    # assumir que é um comando bash
    exec "$@"
fi 