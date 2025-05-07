FROM python:3.9-slim

LABEL maintainer="Embrapa" \
      description="Ambiente para execução dos scripts de integração temática"

# Definindo variáveis para evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Dependências básicas
    wget curl unzip git build-essential pkg-config cmake \
    # Dependências GDAL
    gdal-bin libgdal-dev python3-gdal \
    # Dependências Tesseract OCR
    tesseract-ocr \
    # Dependências para processamento de imagens
    libspatialindex-dev \
    # Limpeza de cache para reduzir o tamanho da imagem
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configurar variáveis de ambiente para GDAL
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal \
    && export C_INCLUDE_PATH=/usr/include/gdal

# Copiar arquivos do projeto
WORKDIR /app
COPY . /app/

# Dar permissão de execução ao script de entrada
RUN chmod +x /app/docker_entrypoint.sh

# Criar pasta para dados e saídas
RUN mkdir -p /data/inputs /data/outputs /data/temp

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir numpy \
    # Instalar GDAL especificando a versão correta
    && gdal-config --version | xargs -I % pip install --no-cache-dir GDAL==% \
    # Instalar as demais dependências do projeto
    && pip install --no-cache-dir \
       pandas \
       geopandas \
       rasterio \
       shapely \
       pyproj \
       sqlalchemy \
       geoalchemy2 \
       psycopg2-binary \
       pytesseract \
       requests \
       matplotlib \
    # Instalar o projeto atual em modo desenvolvimento
    && pip install -e .

# Instalar SICAR diretamente do GitHub (necessário para o script 01)
RUN pip install --no-cache-dir git+https://github.com/urbanogilson/SICAR

# Definir volume para persistência de dados
VOLUME ["/data"]

# Configurar variáveis de ambiente para os scripts
ENV INPUT_DIR=/data/inputs \
    OUTPUT_DIR=/data/outputs \
    TEMP_DIR=/data/temp

# Usar o script de entrada como ponto de entrada
ENTRYPOINT ["/app/docker_entrypoint.sh"]
CMD ["00_Main.py"]

# Exemplo de uso:
# Para construir a imagem:
# docker build -t integracao-tematica .
#
# Para executar o script principal:
# docker run -v $(pwd)/data:/data integracao-tematica
#
# Para executar um script específico:
# docker run -v $(pwd)/data:/data integracao-tematica 01_Download_CAR_estados.py 