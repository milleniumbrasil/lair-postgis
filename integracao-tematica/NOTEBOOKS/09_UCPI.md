# 09_UCPI

**Finalidade**

Este notebook processa dados de Unidades de Conservação de Proteção Integral (UCPI) para:

1. Classificar áreas como UCPI ou não-UCPI
2. Recortar os dados por estados
3. Subdividir por municípios
4. Exportar shapefiles resultantes

## Viabilidade de Conversão para Script Python

**Altamente recomendável converter para script Python** porque:

✔️ O código é 100% processual sem elementos interativos  
✔️ Não utiliza features específicas do Jupyter  
✔️ As operações são autônomas e sequenciais  
✔️ Beneficiaria de um ambiente mais robusto para produção  

## Vantagens da Conversão

1. **Portabilidade**: Executável em qualquer ambiente Python
2. **Performance**: Menos overhead que notebook
3. **Automatização**: Pode ser agendado como job
4. **Monitoramento**: Facilita implementação de logs

## Estrutura Recomendada para o Script Python

```python
import geopandas as gpd
import os
import argparse
from typing import Tuple

def classificar_ucpi(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Classifica áreas como UCPI (1) ou não-UCPI (0)"""
    ucpi = gdf[['UCMI_C', 'UCEI_C', 'UCFI_C', 'geometry']].copy()
    ucpi['CD_UCPI'] = ucpi.apply(
        lambda row: 0 if row['UCMI_C'] == 0 and row['UCEI_C'] == 0 and row['UCFI_C'] == 0 else 1,
        axis=1
    )
    return ucpi.drop(['UCMI_C', 'UCEI_C', 'UCFI_C'], axis=1)

def processar_ucpi(uc_path: str, limites_path: str, output_dir: str):
    """Processa e recorta UCPIs por estados/municípios"""
    # Implementação completa aqui
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--uc', required=True, help='Shapefile de Unidades de Conservação')
    parser.add_argument('--limites', required=True, help='Shapefile de municípios')
    parser.add_argument('--output', required=True, help='Diretório de saída')
    args = parser.parse_args()
    
    processar_ucpi(args.uc, args.limites, args.output)

if __name__ == "__main__":
    main()
```

## Exemplo de Docker-compose.yaml

```yaml
version: '3.8'

services:
  ucpi-processor:
    build: .
    volumes:
      - ./data/input:/app/input
      - ./data/output:/app/output
    environment:
      - PYTHONUNBUFFERED=1
    command: >
      python processar_ucpi.py 
      --uc /app/input/uc.shp 
      --limites /app/input/municipios.shp 
      --output /app/output
```

Com Dockerfile correspondente:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "processar_ucpi.py"]
```

## Conclusão Final

**A conversão para script Python traz benefícios significativos**:

1. **Redução de dependências**: Elimina necessidade de Jupyter
2. **Maior robustez**: Permite tratamento de erros profissional
3. **Escalabilidade**: Pode processar grandes volumes de dados
4. **Monitorabilidade**: Facilita integração com sistemas de logging

**Próximos passos recomendados**:

1. Converter para script .py com funções modularizadas
2. Adicionar:
   - Tratamento de erros detalhado
   - Sistema de logging
   - Validação de inputs
3. Criar imagem Docker otimizada
4. Implementar testes unitários

O código atual tem toda a lógica necessária - a conversão será principalmente uma reorganização estrutural seguindo boas práticas de engenharia de software para produção.
