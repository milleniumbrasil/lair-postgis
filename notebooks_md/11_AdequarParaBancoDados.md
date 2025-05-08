# 11_AdequarParaBancoDados

**Finalidade**

Este notebook padroniza arquivos `shapefile` de **três camadas geoespaciais integradas com CAR** para facilitar sua **inserção posterior em bancos de dados** (ex: PostGIS):

1. **Usos ABC por município** (vários anos)
2. **Declividade**
3. **Aptidão do Solo**

---

### ⚙️ Etapas principais:

| Etapa                    | Descrição                                                                |
| ------------------------ | ------------------------------------------------------------------------ |
| 🧾 Inputs                | Caminhos para pastas contendo shapefiles                                 |
| 🧹 Padronização          | Renomeia colunas para lowercase (`.str.lower()`)                         |
| 🔤 Conversão de encoding | Converte valores da coluna `nom_munici` de `iso-8859-1` para `utf-8`     |
| 📁 Organização           | Cria subpastas por ano para "Usos ABC"                                   |
| 💾 Reescrita             | Salva os arquivos corrigidos com `to_file()` no formato `ESRI Shapefile` |

---

## 🔧 Pode ser convertido em script `.py` local e autônomo?

**Sim, totalmente.** As modificações são simples:

| Atual                        | Substituir por...                                             |
| ---------------------------- | ------------------------------------------------------------- |
| `input()`                    | `argparse` ou `.env` com `os.getenv()`                        |
| Caminhos fixos (`rf'{...}'`) | `os.path.join()` (mais robusto e multiplataforma)             |
| Encoding manual              | Pode ser generalizado para múltiplas colunas com `try-except` |

---

## 🐳 Pode ser incluído em deploy com Docker Compose?

### ✅ **Sim.**

#### Dependências:

* Python 3.10+
* `geopandas`, `fiona`, `shapely`, `pyproj`, `gdal`
* Volume contendo os shapefiles a serem ajustados

#### Exemplo `Dockerfile`:

```dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev \
    && pip install --no-cache-dir geopandas numpy

COPY ajusta_colunas.py /app/
WORKDIR /app
ENTRYPOINT ["python", "ajusta_colunas.py"]
```

#### Exemplo `docker-compose.yaml`:

```yaml
services:
  ajustes-shapefile:
    build: .
    volumes:
      - ./dados:/data
    command: [
      "--uso_path", "/data/uso",
      "--decl_path", "/data/decliv",
      "--edafo_path", "/data/aptidao"
    ]
```

---

## 💡 Conclusão

✅ **Este notebook deve ser convertido em script `.py` independente.**

**Motivos para converter:**

* **Evita dependência de Jupyter/Colab**
* **Executável por linha de comando**
* **Mais fácil de automatizar com CI/CD ou cronjobs**
* **Pode ser empacotado via Docker para replicabilidade e reuso**

---

### 📌 Recomendação Final

**Sim, vale a pena migrar para um script `.py`,** especialmente se for parte de um pipeline de preparação e carregamento de dados geográficos em sistemas da Embrapa.


