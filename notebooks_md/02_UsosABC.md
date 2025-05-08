# 02_UsosABC

**Finalidade**

O notebook realiza uma **pipeline de processamento geoespacial** que:
- Recorta rasters do MapBiomas por município.
- Reclassifica usos do solo (ABC: Agricultura, Pecuária, Florestas).
- Integra com dados do CAR (Cadastro Ambiental Rural).
- Gera shapefiles finais por município e ano.

#### Problemas com o Formato Notebook
- **Dependência de ambientes interativos** (Jupyter/Colab):  
  O código está fragmentado em células, com inputs manuais (`input()`) e sem tratamento robusto de erros.

- **Falta de modularização**:  
  Toda a lógica está em um único fluxo linear, difícil de reutilizar ou testar.

- **Dificuldade para deploy**:  
  Notebooks não são ideais para produção (ex: rodar em containers, agendamento via cron).

---

### **Como Transformar em um Script Python Independente**
#### **Melhorias Necessárias**
1. **Substituir `input()` por parâmetros**:
   - Usar `argparse` ou um arquivo de configuração (ex: `config.yaml`).

2. **Modularizar funções**:
   - Separar em funções específicas (ex: `recortar_rasters()`, `reclassificar_usos()`).

3. **Adicionar logs**:
   - Trocar `print()` por `logging` para rastreamento.

4. **Gerenciar paths dinamicamente**:
   - Usar `pathlib.Path` em vez de concatenação de strings.

#### **Exemplo de Estrutura para o Script**:
```python
# usos_abc.py
import argparse
from pathlib import Path
import logging

def main(config):
    logging.info("Iniciando processamento...")
    recortar_rasters(config.originais_path, config.limites_path)
    gerar_usos_abc(config.temp_path, config.out_path)
    integrar_car(config.car_path, config.final_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--originais_path", type=Path, required=True)
    parser.add_argument("--limites_path", type=Path, required=True)
    parser.add_argument("--car_path", type=Path, required=True)
    parser.add_argument("--output_dir", type=Path, default=Path("output"))
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    main(args)
```

---

### **Integração com Docker**
#### **`Dockerfile` Exemplo**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt  # (rasterio, geopandas, etc.)

COPY usos_abc.py .
COPY config.yaml .

CMD ["python", "usos_abc.py", "--originais_path", "/data/originais", "--output_dir", "/data/output"]
```

#### **`docker-compose.yaml` Exemplo**
```yaml
version: '3.8'
services:
  usos-abc:
    build: .
    volumes:
      - ./data/input:/data/originais
      - ./data/output:/data/output
    environment:
      - GDAL_DATA=/usr/share/gdal
```

---

### **Vantagens da Migração para Script + Docker**
1. **Portabilidade**:  
   Roda em qualquer sistema com Docker/Python, sem depender de Jupyter.

2. **Automatização**:  
   Pode ser agendado (ex: cron no container) ou integrado a pipelines (Airflow).

3. **Versionamento**:  
   Scripts são mais fáceis de versionar no Git que notebooks.

4. **Performance**:  
   Elimina overhead do notebook (útil para processamento pesado).

---

### **Conclusão: Vale a Penha Migrar?**
| **Critério**               | **Notebook**                          | **Script Python + Docker**             |
|----------------------------|---------------------------------------|----------------------------------------|
| **Facilidade de desenvolvimento** | ✅ Melhor para prototipagem          | ⚠️ Requer mais estrutura inicial      |
| **Deploy em produção**      | ❌ Frágil, difícil de automatizar     | ✅ Ideal para containers e pipelines   |
| **Manutenção**             | ❌ Código menos organizado            | ✅ Funções modulares e logs            |
| **Offline**                | ⚠️ Depende do kernel Jupyter         | ✅ Totalmente independente             |

#### **Recomendação Final**
**Migre para um script Python + Docker se**:
- Você precisa rodar o processo **automaticamente** (ex: todo mês com novos dados).
- Quer integrá-lo a um **sistema maior** (ex: ETL com Airflow).
- Precisa de **confiabilidade** (logs, tratamento de erros).

**Mantenha como notebook se**:
- É um projeto **exploratório** (ex: análise pontual).
- A equipe só sabe trabalhar com Jupyter.

#### **Passo a Passo para Migração**
1. Quebre o notebook em funções em um `.py`.
2. Substitua `input()` por argumentos/arquivos de configuração.
3. Adicione logs e tratamento de erros.
4. Containerize com Docker.
5. Monte um volume para dados de entrada/saída.
