# 12_To_PostGis

**Finalidade**

Este notebook serve para **importar shapefiles georreferenciados** (GeoDataFrames) para um banco de dados **PostgreSQL/PostGIS**, convertendo as geometrias para o formato WKT (`Well-Known Text`) com SRID 4326.

---

### 🔍 Etapas executadas

| Etapa                    | Descrição                                                                |
| ------------------------ | ------------------------------------------------------------------------ |
| 📦 **Carregamento**      | Importa shapefiles de uma pasta específica                               |
| 🌍 **CRS fixo**          | Reprojeta todos os dados para WGS84 (EPSG:4326)                          |
| 📐 **Explode**           | Divide geometrias multipartidas                                          |
| 🧱 **Padroniza colunas** | Nomes de colunas convertidos para lowercase                              |
| 🧬 **Transformação**     | Cria coluna `geom` com WKTElement para `GeoAlchemy2`                     |
| 🗃️ **Upload**           | Insere os dados na tabela `schema.table` do PostgreSQL usando `to_sql()` |

---

## 🛠️ Pode ser convertido em script `.py` autônomo?

✅ **Sim, com tranquilidade.**
Este é um caso claro de tarefa automatizável, ideal para:

* Integração em pipelines ETL
* Execução via `cron`, `Airflow`, ou CI/CD
* Dockerização completa

Recomenda-se:

* Substituir `input()` por `argparse` ou variáveis de ambiente (`dotenv`, `os.getenv`)
* Permitir múltiplos diretórios/tabelas
* Adicionar logs e tratamento de erros

---

## 🐳 Pode ser incluído em um `docker-compose.yaml`?

✅ **Sim.**
Você pode:

1. Incluir esse script em um contêiner Python com `GeoAlchemy2`, `SQLAlchemy`, `geopandas`
2. Adicionar um volume com os arquivos `.shp`
3. Garantir que o contêiner do PostgreSQL esteja disponível via rede Docker

---

### 💡 Exemplo simplificado de `Dockerfile`:

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gdal-bin libgdal-dev \
    && pip install --no-cache-dir geopandas sqlalchemy psycopg2-binary geoalchemy2

COPY upload_shapefiles.py /app/
WORKDIR /app
ENTRYPOINT ["python", "upload_shapefiles.py"]
```

---

### 💡 Exemplo `docker-compose.yaml`:

```yaml
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

  uploader:
    build: .
    depends_on:
      - postgis
    volumes:
      - ./dados:/data
    environment:
      - DB_HOST=postgis
      - DB_PORT=5432
      - DB_NAME=lair
      - DB_USER=postgres
      - DB_PASS=postgres
      - DATA_PATH=/data/Usos_ABC_Municipios/2021
      - DB_SCHEMA=Usos_ABC
      - DB_TABLE=2021
```

---

## 📌 Conclusão

✅ **Sim, vale a pena converter este notebook para `.py`** e empacotá-lo em um contêiner Docker.

**Benefícios:**

* Portabilidade (roda local, servidor, CI/CD, etc.)
* Automação do upload de dados geoespaciais
* Eliminação da dependência de Jupyter
* Integração fácil com pipelines e agendadores


