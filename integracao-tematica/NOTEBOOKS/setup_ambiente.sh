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
    "paths": {
        "input": "/data/inputs",
        "output": "/data/outputs",
        "temp": "/data/temp"
    },
    "postgres": {
        "host": "",
        "port": 5432,
        "database": "",
        "user": "",
        "password": ""
    }
}
EOL
fi

echo -e "${BLUE}Preparando arquivos de dados de exemplo...${NC}"
# Criar arquivos README explicativos nos diretórios de dados
cat > data/inputs/README.txt << EOL
Diretório para arquivos de entrada.
Coloque aqui os arquivos necessários para o processamento dos scripts.
EOL

cat > data/outputs/README.txt << EOL
Diretório para arquivos de saída.
Os resultados do processamento serão salvos aqui.
EOL

cat > data/temp/README.txt << EOL
Diretório para arquivos temporários.
Arquivos intermediários do processamento serão salvos aqui.
EOL

echo -e "${GREEN}Construindo a imagem Docker...${NC}"
docker-compose build

echo -e "${BLUE}==================================================================${NC}"
echo -e "${GREEN}AMBIENTE CONFIGURADO COM SUCESSO!${NC}"
echo -e "${BLUE}==================================================================${NC}"
echo -e "${YELLOW}Para executar todos os scripts em sequência:${NC}"
echo "docker-compose up --abort-on-container-exit"
echo -e "${YELLOW}Para executar um script específico:${NC}"
echo "docker-compose run --rm integracao-tematica 01_Download_CAR_estados.py"
echo -e "${YELLOW}Para acessar o shell do container:${NC}"
echo "docker-compose run --rm integracao-tematica bash"
echo -e "${BLUE}==================================================================${NC}"
echo -e "${YELLOW}Importante:${NC} O contêiner se desligará automaticamente após concluir os scripts."
echo -e "${BLUE}==================================================================${NC}" 