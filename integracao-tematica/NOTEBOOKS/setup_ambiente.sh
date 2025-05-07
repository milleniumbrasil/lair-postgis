#!/bin/bash
set -e

# Cores para formatação de saída
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}==================================================================${NC}"
echo -e "${GREEN}    CONFIGURAÇÃO DO AMBIENTE PARA INTEGRAÇÃO TEMÁTICA${NC}"
echo -e "${BLUE}==================================================================${NC}"

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}Docker não encontrado. Por favor, instale o Docker:${NC}"
    echo "https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar se o Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo -e "${YELLOW}Docker Compose não encontrado. Por favor, instale o Docker Compose:${NC}"
    echo "https://docs.docker.com/compose/install/"
    exit 1
fi

echo -e "${GREEN}Criando estrutura de diretórios...${NC}"
# Criar diretórios necessários
mkdir -p data/inputs data/outputs data/temp config

# Verificar se existem arquivos de configuração e criar exemplos se necessário
if [ ! -f "config/config.json" ]; then
    echo -e "${BLUE}Criando arquivo de configuração exemplo...${NC}"
    cat > config/config.json << EOL
{
    "postgres": {
        "host": "postgis",
        "port": 5432,
        "database": "lair",
        "user": "postgres",
        "password": "postgres"
    },
    "paths": {
        "input": "/data/inputs",
        "output": "/data/outputs",
        "temp": "/data/temp"
    }
}
EOL
fi

echo -e "${GREEN}Construindo a imagem Docker...${NC}"
docker-compose build

echo -e "${BLUE}==================================================================${NC}"
echo -e "${GREEN}AMBIENTE CONFIGURADO COM SUCESSO!${NC}"
echo -e "${BLUE}==================================================================${NC}"
echo -e "${YELLOW}Para executar todos os scripts:${NC}"
echo "docker-compose up"
echo -e "${YELLOW}Para executar um script específico:${NC}"
echo "docker-compose run --rm integracao-tematica 01_Download_CAR_estados.py"
echo -e "${YELLOW}Para acessar o shell:${NC}"
echo "docker-compose run --rm integracao-tematica bash"
echo -e "${YELLOW}Para acessar o PgAdmin:${NC}"
echo "http://localhost:5050 (login: admin@embrapa.br, senha: admin)"
echo -e "${BLUE}==================================================================${NC}" 