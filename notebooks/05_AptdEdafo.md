# 05_AptdEdafo

**Finalidade**

Este notebook processa **arquivos shapefile de Aptidão de Solo** (corrigidos por estado) e os recorta para **cada município**, integrando com os dados do **CAR (Cadastro Ambiental Rural)**.

### 🚧 Etapas principais:

1. **Entrada de diretórios**: via `input()` (usuário manualmente fornece caminhos).
2. **Leitura e reprojeção do shapefile de municípios**.
3. **Recorte dos shapefiles de aptidão solo por município**.
4. **Renomeação de arquivos `AREA_IMOVEL`** (do CAR).
5. **Interseção espacial (overlay)** de:

   * Aptidão de Solo (`Aptd_Edafo`)
   * Área dos Imóveis Rurais (`AREA_IMOVEL`)
6. **Exportação final dos shapefiles integrados para diretório `Aptd_Edafo_Municipios_CAR/`**.

---

## 📦 Dependências

* `geopandas`, `numpy`, `glob`, `os`
* Dados: shapefiles com codificação padronizada (`_corrigido.shp`, `AREA_IMOVEL` etc.)

---

## 🔁 Pode ser convertido em script `.py` executável offline?

**Sim, perfeitamente.** As únicas adaptações necessárias são:

| Elemento atual                              | Substituir por...                      |
| ------------------------------------------- | -------------------------------------- |
| `input()` para caminhos                     | `argparse` ou variáveis fixas          |
| Reprojeção automática                       | Garantir coerência no `to_crs()`       |
| Hardcoded `"\\{...}"` (problemas de escape) | `os.path.join()` ou `f"{...}"` com `/` |
| Manipulação interativa (Jupyter)            | Executar diretamente via terminal      |

---

## 🚢 Pode ser parte de um `deploy` com Docker Compose?

**Sim**, com estas observações:

### ✅ **Sim, desde que:**

1. Os dados (`.shp`) estejam em **volumes montados** (`./dados:/data`).
2. O script seja refeito como CLI:

   ```bash
   python recorte_aptidao.py --dirpath /data --originais /data/aptidao --car /data/car --limites /data/municipios.shp
   ```
3. A imagem Docker contenha:

   * `geopandas`
   * `fiona`, `shapely`, `pyproj`, `gdal`
   * Python 3.10+

### 📄 Exemplo `Dockerfile`:

```Dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gdal-bin libgdal-dev python3-gdal \
    && pip install --no-cache-dir geopandas numpy

COPY recorte_aptidao.py /app/
WORKDIR /app
ENTRYPOINT ["python", "recorte_aptidao.py"]
```

### 📄 Exemplo `docker-compose.yaml`:

```yaml
services:
  recorte-aptidao:
    build: .
    volumes:
      - ./dados:/data
    command: ["--dirpath", "/data", "--originais", "/data/aptidao", "--car", "/data/car", "--limites", "/data/municipios.shp"]
```

---

## ⚠️ Possíveis ajustes:

1. Tratar **warnings de CRS incompatível**:

   * Unificar via: `to_crs(lim.crs)` ou `to_crs(epsg=4326)`
2. Evitar sobrescrita de variáveis (ex: `car = glob.glob(...)` conflita com a lib `car`).
3. Substituir `rf'{...}'` com `os.path.join()`.

---

## 🧾 Conclusão

✅ **Sim, este notebook pode (e deve) ser convertido em um script `.py` reutilizável, autônomo e parte de um pipeline com Docker.**

**Vantagens de converter:**

* Automatização via CLI
* Padronização de execução
* Reutilização por outros sistemas
* Facilidade de integração em pipelines CI/CD ou rotinas periódicas

Se desejar, posso:

* Reescrever esse notebook em um `recorte_aptidao.py`
* Gerar o `Dockerfile` e `docker-compose.yaml`
* Eliminar interatividade (`input()`)


