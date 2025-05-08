# 07_AmazoniaLegal

**Finalidade**

Este notebook realiza operações de geoprocessamento para:

1. Recortar a base da Amazônia Legal por estados
2. Subdividir os recortes estaduais por municípios
3. Exportar os resultados em shapefiles

## Viabilidade de Conversão para Script Python

**É altamente recomendável converter para um script Python independente** porque:

✔️ Todas as operações são sequenciais e autônomas  
✔️ Não há elementos interativos ou de visualização  
✔️ O código já está estruturado de forma linear  
✔️ Não utiliza recursos específicos do Jupyter  

## Vantagens da Conversão

1. **Portabilidade**: Executável em qualquer ambiente Python
2. **Performance**: Elimina overhead do notebook
3. **Automatização**: Facilita integração com pipelines ETL
4. **Containerização**: Simplifica a criação de imagens Docker

## Estrutura Recomendada para o Script Python

```python
import geopandas as gpd
import os
import glob
import argparse

def processar_amazonia_legal(amz_path, limites_path, output_dir):
    """Processa a base da Amazônia Legal por estados e municípios"""
    # Implementação da lógica principal
    pass

def main():
    parser = argparse.ArgumentParser(description='Recorta base da Amazônia Legal por estados e municípios')
    parser.add_argument('--amz', required=True, help='Shapefile da Amazônia Legal')
    parser.add_argument('--limites', required=True, help='Shapefile de municípios')
    parser.add_argument('--output', required=True, help='Diretório de saída')
    args = parser.parse_args()
    
    processar_amazonia_legal(args.amz, args.limites, args.output)

if __name__ == "__main__":
    main()
```

## Exemplo de Docker-compose.yaml

```yaml
version: '3.8'

services:
  amazonia-legal:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ./dados:/app/dados
    environment:
      - PYTHONUNBUFFERED=1
    command: python processar_amazonia.py --amz /app/dados/amazonia_legal.shp --limites /app/dados/municipios.shp --output /app/dados/saida
```

Com Dockerfile correspondente:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "processar_amazonia.py"]
```

## Conclusão Final

**A conversão para script Python é altamente benéfica** porque:

1. **Reduz dependências**: Elimina necessidade de Jupyter/Colab
2. **Facilita deploy**: Pode ser executado como serviço ou job
3. **Melhora robustez**: Permite adicionar tratamento de erros
4. **Otimiza recursos**: Consome menos memória que notebook

**Próximos passos recomendados:**
1. Converter para script .py com tratamento de erros
2. Adicionar sistema de logging
3. Implementar verificação de inputs
4. Criar Dockerfile básico
5. Testar em ambiente isolado

O código atual já contém toda a lógica necessária - a conversão será principalmente uma reorganização estrutural com adição de boas práticas de engenharia de software.
