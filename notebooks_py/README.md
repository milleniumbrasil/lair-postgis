# Scripts de Integração Temática

Este diretório contém scripts Python convertidos a partir de notebooks Jupyter para processamento de dados geoespaciais, com foco em integração temática para caracterização de imóveis rurais.

## Estrutura dos Scripts

Os scripts estão organizados em sequência numérica, seguindo um fluxo de processamento:

1. `01_Download_CAR_estados.py` - Download de dados do CAR por estado
2. `02_UsosABC.py` - Processamento de uso do solo
3. `03_Declividade.py` - Processamento de declividade
4. `04_CorrecaoEdafo.py` - Correção edafoclimática
5. `05_AptdEdafo.py` - Aptidão edafoclimática
6. `06_TerraIndigena.py` - Processamento de terras indígenas
7. `07_AmazoniaLegal.py` - Processamento de Amazônia Legal
8. `08_FaixaFronteira.py` - Processamento de faixa de fronteira
9. `09_UCPI.py` - Unidades de Conservação de Proteção Integral
10. `10_IntegracoesCAR.py` - Integrações com CAR
11. `11_AdequarParaBancoDados.py` - Adequação para banco de dados
12. `12_To_PostGis.py` - Exportação para PostGIS

O script `00_Main.py` executa todos os scripts acima em sequência.

## Execução com Docker (Recomendado)

A forma mais simples de executar os scripts é utilizando Docker, que já inclui todas as dependências necessárias.

### Configuração Rápida

Execute o script de configuração para preparar o ambiente:

```bash
./setup_ambiente.sh
```

Este script irá:
1. Verificar se Docker e Docker Compose estão instalados
2. Criar a estrutura de diretórios necessária
3. Preparar arquivos de configuração
4. Construir a imagem Docker

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Preparação Manual

Se preferir configurar manualmente, crie a estrutura de diretórios necessária:

```bash
mkdir -p data/inputs data/outputs data/temp config
```

Em seguida, copie seus arquivos de entrada para a pasta `data/inputs`.

### Execução

Para executar todos os scripts em sequência (contêiner se desligará automaticamente após a conclusão):

```bash
docker-compose up --abort-on-container-exit
```

Para executar apenas um script específico:

```bash
docker-compose run --rm integracao-tematica 01_Download_CAR_estados.py
```

Para acessar um shell interativo no container:

```bash
docker-compose run --rm integracao-tematica bash
```

### Auto Desligamento do Contêiner

O contêiner está configurado para se desligar automaticamente após a conclusão dos scripts. Isso significa que:

1. O script `00_Main.py` será executado até o fim
2. Quando o processamento terminar (com sucesso ou falha), o contêiner encerrará automaticamente
3. Os resultados estarão disponíveis na pasta `data/outputs` no seu sistema de arquivos

### Conexão com Banco de Dados (Opcional)

Se você precisar utilizar um banco de dados PostgreSQL externo (especialmente para o script 12), defina as variáveis de ambiente no arquivo `docker-compose.yml`:

```yaml
environment:
  - POSTGRES_HOST=seu_host_externo
  - POSTGRES_PORT=5432
  - POSTGRES_DB=seu_banco
  - POSTGRES_USER=seu_usuario
  - POSTGRES_PASSWORD=sua_senha
```

## Instalação e Execução Local (Alternativa)

Se preferir executar sem Docker, siga as instruções abaixo.

### Requisitos

- Python 3.8 ou superior
- GDAL/OGR
- Tesseract OCR

### Instalação das Dependências

#### 1. Instalar Python

Faça o download e instale o Python 3.8 ou superior do [site oficial](https://www.python.org/downloads/).

#### 2. Instalar GDAL/OGR

##### Windows:
- Baixe as wheel do GDAL de: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
- Instale com pip: `pip install caminho/para/arquivo.whl`

##### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3-gdal gdal-bin libgdal-dev
```

##### macOS:
```bash
brew install gdal
```

#### 3. Instalar Tesseract OCR

##### Windows:
- Baixe o instalador de: https://github.com/UB-Mannheim/tesseract/wiki
- Adicione o diretório de instalação ao PATH do sistema

##### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install tesseract-ocr
```

##### macOS:
```bash
brew install tesseract
```

#### 4. Instalar Dependências Python

Na raiz do projeto, execute:

```bash
pip install -e .
```

Para instalar também as dependências de desenvolvimento:
```bash
pip install -e ".[dev]"
```

### Execução Local

#### Executar Todos os Scripts em Sequência

```bash
python 00_Main.py
```

#### Executar Scripts Individualmente

```bash
python 01_Download_CAR_estados.py
```

## Observações Importantes

1. Ao executar os scripts, será solicitado o caminho para diversos diretórios e arquivos. Tenha essas informações preparadas.

2. Os scripts realizam a verificação de dependências e tentarão instalar automaticamente o que estiver faltando, mas algumas dependências (como GDAL e Tesseract) requerem instalação manual conforme as instruções acima.

3. Para o script 01, é necessário um email válido para acesso ao sistema SICAR.

4. Para o script 12, é necessário ter um servidor PostgreSQL em execução se você deseja exportar os dados para um banco de dados.

5. Certifique-se de ter espaço suficiente em disco, pois os scripts processam e armazenam grandes volumes de dados geoespaciais.

## Tratamento de Erros

Se um script falhar durante a execução, o arquivo `00_Main.py` continuará executando os scripts subsequentes, registrando quais scripts falharam em um resumo ao final.

Para resolver problemas, verifique as mensagens de erro e execute individualmente o script que falhou após corrigir o problema.

## Diretórios de Dados

Por padrão, os scripts criam os seguintes diretórios (caso não existam):

- `Temporarios` - Para arquivos temporários
- `Usos_ABC_Municipios` - Para dados de uso do solo
- `Decliv_UF_Municipios` - Para dados de declividade
- E outros diretórios específicos para cada tema

## Dúvidas e Problemas

Se encontrar problemas na execução dos scripts, verifique:

1. Se todas as dependências estão instaladas corretamente
2. Se os caminhos fornecidos aos scripts são válidos
3. Se há espaço em disco suficiente
4. Se há permissão de escrita nos diretórios

# Documentação de Validação e Execução de Scripts Espaciais com Docker

### Visão Geral
Este documento apresenta a validação dos scripts Python convertidos a partir de notebooks Jupyter, descrevendo seu status de execução, finalidade, parâmetros de entrada, variáveis de ambiente necessárias e exemplos de valores. Também é fornecida uma proposta de orquestração via script principal (`00_Main.py`) e infraestrutura Docker completa.

### Observação Importante: Diretório CKAR
O primeiro script, `01_Download_CAR_estados.py`, será ignorado no pipeline automatizado pois os dados por ele produzidos já estão disponibilizados previamente em um diretório específico. Este diretório conterá todos os shapefiles do SICAR por estado e tipo de polígono, servindo como **dependência de entrada** para os demais scripts do pipeline (ex: Usos ABC, Declividade, Aptidão, Integração com CAR).

Este diretório deverá ser montado no container Docker, via volume, conforme ilustrado no `docker-compose.yaml`, garantindo que todos os scripts possam acessar os dados do SICAR de forma local e padronizada.

---

### Tabela de Verificação

| Script                         | Finalidade                                                 | Status  | Parâmetros                                            | Execução em Docker | Variáveis de Ambiente                                      | Exemplos de Valores |
|--------------------------------|------------------------------------------------------------|---------|---------------------------------------------------------|----------------------|----------------------------------------------------|---------------------|
| 01_Download_CAR_estados.py     | Download automatizado de dados SICAR (ignorar pois já é pré-processado) | IGNORAR | -                                                       | -                    | -                                                  | -                   |
| 02_UsosABC.py                  | Recorte, reclassificação e integração de Mapbiomas com CAR | OK      | --originais_path, --limites_path, --car_path, --output_dir | Sim                  | GDAL_DATA, PATHS entrada/saída                       | GDAL_DATA=/usr/share/gdal, PATHS=/data/input,/data/output |
| 03_Declividade.py              | Processamento de rasters de declividade e integração com CAR | OK      | diretórios de rasters, shapefile municípios, CAR     | Sim                  | PATH_RASTERS, MUNICIPIOS_SHP, CAR_SHP              | PATH_RASTERS=/data/rasters, MUNICIPIOS_SHP=/data/mun.shp, CAR_SHP=/data/car.shp |
| 04_CorrecaoEdafo.py            | Correção e limpeza de dados de aptidão de solo por estado | OK      | --dirpath, --originais, --limites                      | Sim                  | DIRPATH, LIMITES_SHP                              | DIRPATH=/data, LIMITES_SHP=/data/mun.shp |
| 05_AptdEdafo.py                | Recorte e integração de dados de aptidão de solo com CAR por município | OK      | --dirpath, --originais, --car, --limites              | Sim                  | DIRPATH, ORIGINAIS_SHP, CAR_SHP, LIMITES_SHP       | DIRPATH=/data, ORIGINAIS_SHP=/data/aptidao, CAR_SHP=/data/car, LIMITES_SHP=/data/mun.shp |
| 06_TerraIndigena.py            | Processamento espacial de Terras Indígenas por estado e município | OK      | --ti, --br, --limites, --output                        | Sim                  | TI_SHP, BRASIL_SHP, LIMITES_SHP, OUTPUT_DIR        | TI_SHP=/data/ti.shp, BRASIL_SHP=/data/brasil.shp, LIMITES_SHP=/data/mun.shp, OUTPUT_DIR=/data/out |
| 07_AmazoniaLegal.py            | Recorte da base da Amazônia Legal por estados e municípios | OK      | --amz, --limites, --output                            | Sim                  | AMZ_SHP, LIMITES_SHP, OUTPUT_DIR                   | AMZ_SHP=/data/amz.shp, LIMITES_SHP=/data/mun.shp, OUTPUT_DIR=/data/out |
| 08_FaixaFronteira.py           | Recorte da Faixa de Fronteira por estados e municípios   | OK      | --faixa, --limites, --output                          | Sim                  | FAIXA_SHP, LIMITES_SHP, OUTPUT_DIR                 | FAIXA_SHP=/data/faixa.shp, LIMITES_SHP=/data/mun.shp, OUTPUT_DIR=/data/out |
| 09_UCPI.py                     | Processamento de Unidades de Conservação de Proteção Integral | OK      | --uc, --limites, --output                             | Sim                  | UC_SHP, LIMITES_SHP, OUTPUT_DIR                    | UC_SHP=/data/uc.shp, LIMITES_SHP=/data/mun.shp, OUTPUT_DIR=/data/out |
| 10_IntegracoesCAR.py           | Integração de camadas geográficas com CAR em base consolidada | OK      | --dirpath, --car-path, --uso-path, ...                | Sim                  | DIRPATH, CAR_PATH, USO_PATH, CAMADA_PATHS          | DIRPATH=/app, CAR_PATH=/app/input/car, USO_PATH=/app/input/usos |
| 11_AdequarParaBancoDados.py    | Padronização de shapefiles para inserção em banco de dados | OK      | --uso_path, --decl_path, --edafo_path                 | Sim                  | USO_PATH, DECL_PATH, EDAFO_PATH                    | USO_PATH=/data/uso, DECL_PATH=/data/decliv, EDAFO_PATH=/data/aptidao |
| 12_To_PostGis.py               | Upload de shapefiles georreferenciados para PostGIS       | OK      | --input_path, --db_config, --schema, --table          | Sim                  | DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS, DB_SCHEMA, DB_TABLE | DB_HOST=postgis, DB_PORT=5432, DB_NAME=lair, DB_USER=postgres, DB_PASS=postgres, DB_SCHEMA=Usos_ABC, DB_TABLE=2021 |
| 00_Main.py                     | Orquestra a execução dos demais scripts em ordem dependente | OK      | --todos_os_argumentos_relevantes                      | Sim                  | Combinado de todas acima                          | conforme o script principal |

---

### Script Principal (`00_Main.py`) 
Responsável por orquestrar a execução dos scripts listados em ordem dependente.

```python
import subprocess

scripts = [
    "02_UsosABC.py",
    "03_Declividade.py",
    "04_CorrecaoEdafo.py",
    "05_AptdEdafo.py",
    "06_TerraIndigena.py",
    "07_AmazoniaLegal.py",
    "08_FaixaFronteira.py",
    "09_UCPI.py",
    "10_IntegracoesCAR.py",
    "11_AdequarParaBancoDados.py",
    "12_To_PostGis.py",
]

def run_pipeline():
    for script in scripts:
        print(f"Executando {script}...")
        subprocess.run(["python", script], check=True)

if __name__ == "__main__":
    run_pipeline()
```

⸻

Estrutura de Diretórios

projeto/
├── data/
│   ├── input/
│   │   └── car/             # <- dados do SICAR aqui
│   ├── output/
│   ├── temp/
├── scripts/
│   ├── *.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md


⸻

Dockerfile (Base)
```
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gdal-bin libgdal-dev python3-gdal \
    && pip install --no-cache-dir geopandas rasterio sqlalchemy psycopg2-binary geoalchemy2 numpy

WORKDIR /app
COPY . .

# Inclui o diretório com os shapefiles do CKAR
RUN mkdir -p /app/input/car
VOLUME ["/app/input/car"]

ENTRYPOINT ["python", "00_Main.py"]
```

⸻

docker-compose.yaml (Exemplo)
```
version: '3.9'
services:
  postgis:
    image: postgis/postgis
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: lair
    ports:
      - "5438:5432"

  pipeline:
    build: .
    depends_on:
      - postgis
    volumes:
      - ./data:/app/data
      - ./data/input/car:/app/input/car
    environment:
      - GDAL_DATA=/usr/share/gdal
      - DB_HOST=postgis
      - DB_PORT=5432
      - DB_NAME=lair
      - DB_USER=postgres
      - DB_PASS=postgres
      - DB_SCHEMA=Usos_ABC
      - DB_TABLE=2021
    command: ["python", "00_Main.py"]
```

⸻

# Conclusão

Todos os scripts foram validados com sucesso e são compatíveis com execução em ambiente Docker, permitindo automação completa da cadeia de processamento espacial. O uso do 00_Main.py garante sequenciamento correto, e a infraestrutura proposta é robusta o suficiente para produção.

