FROM jupyter/scipy-notebook:latest

USER root

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configurar variáveis de ambiente GDAL
ENV GDAL_VERSION=3.6.2
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Instalar dependências Python
RUN pip install --no-cache-dir \
    papermill \
    geopandas \
    rasterio \
    psycopg2-binary \
    geoalchemy2 \
    notebook \
    nbformat \
    nbconvert \
    ipykernel

# Configurar diretórios de trabalho
WORKDIR /home/jovyan/work

# Criar diretórios para entrada/saída e notebooks
RUN mkdir -p /home/jovyan/data/input /home/jovyan/data/output /home/jovyan/work/notebooks

# Copiar arquivos necessários
COPY notebooks/*.ipynb ./
COPY notebooks/run_notebooks.py ./

# Configurar variáveis de ambiente
ENV INPUT_PATH=/home/jovyan/data/input
ENV OUTPUT_PATH=/home/jovyan/data/output
ENV PYTHONUNBUFFERED=1

# Comando para executar o processamento
CMD ["python", "run_notebooks.py"]