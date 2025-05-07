#!/bin/bash
set -e

# Definir caminhos padrão caso não estejam definidos
INPUT_DIR=${INPUT_DIR:-"/data/inputs"}
OUTPUT_DIR=${OUTPUT_DIR:-"/data/outputs"}
TEMP_DIR=${TEMP_DIR:-"/data/temp"}

# Criar diretórios se não existirem
mkdir -p $INPUT_DIR $OUTPUT_DIR $TEMP_DIR

# Configurar variáveis de ambiente PostgreSQL
export POSTGRES_HOST=${POSTGRES_HOST:-"postgis"}
export POSTGRES_PORT=${POSTGRES_PORT:-"5432"}
export POSTGRES_DB=${POSTGRES_DB:-"lair"}
export POSTGRES_USER=${POSTGRES_USER:-"postgres"}
export POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-"postgres"}

# Exibir configurações
echo "================================================================"
echo "Configurações do ambiente:"
echo "----------------------------------------------------------------"
echo "Diretório de entrada: $INPUT_DIR"
echo "Diretório de saída: $OUTPUT_DIR"
echo "Diretório temporário: $TEMP_DIR"
echo "Banco de dados: $POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"
echo "================================================================"

# Verificar se existe o script solicitado
if [ -f "$1" ]; then
    echo "Executando script: $1"
    # Executar o script Python
    python "$@"
else
    # Se o primeiro argumento não for um script existente, 
    # assumir que é um comando bash
    exec "$@"
fi 