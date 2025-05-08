# 06_TerraIndigena

**Finalidade**

Este notebook Jupyter realiza operações de geoprocessamento para:

1. Adequar a base de Terras Indígenas
2. Recortar os dados por estados e municípios
3. Realizar operações espaciais (diferença, merge, clip)
4. Ajustar atributos e codificação

## Viabilidade de Conversão para Script Python

**É altamente recomendável converter para um script Python independente** porque:

1. O notebook não utiliza nenhum recurso específico do Jupyter
2. Todas as operações são sequenciais e autônomas
3. O código já está estruturado em blocos lógicos claros
4. Não há elementos interativos ou de visualização

## Vantagens da Conversão

1. **Portabilidade**: Execução em qualquer ambiente Python sem dependências extras
2. **Performance**: Elimina overhead do notebook
3. **Automatização**: Facilita agendamento e integração com pipelines
4. **Containerização**: Simplifica a criação de imagens Docker

## Estrutura Recomendada para o Script Python

```python
import geopandas as gpd
import os
import glob
import argparse

def processar_terras_indigenas(ti_path, br_path, limites_path, output_dir):
    # Implementar a lógica principal aqui
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ti', required=True, help='Caminho do shapefile de Terras Indígenas')
    parser.add_argument('--br', required=True, help='Caminho do shapefile do Brasil')
    parser.add_argument('--limites', required=True, help='Caminho do shapefile de municípios')
    parser.add_argument('--output', required=True, help='Diretório de saída')
    args = parser.parse_args()
    
    processar_terras_indigenas(args.ti, args.br, args.limites, args.output)

if __name__ == "__main__":
    main()
```

## Exemplo de Docker-compose.yaml

```yaml
version: '3.8'

services:
  terras-indigenas:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ./dados:/app/dados
    environment:
      - PYTHONUNBUFFERED=1
    command: python processar_terras_indigenas.py --ti /app/dados/tis_poligonais.shp --br /app/dados/brasil.shp --limites /app/dados/municipios.shp --output /app/dados/saida
```

Com um Dockerfile correspondente:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "processar_terras_indigenas.py"]
```

## Conclusão Final

**A conversão para script Python é altamente recomendada** porque:

✔️ Elimina a dependência desnecessária de ambientes Jupyter  
✔️ Facilita a implantação em produção  
✔️ Permite execução em servidores headless  
✔️ Simplifica a integração com outros sistemas  
✔️ Melhora a manutenibilidade  

**Próximos passos sugeridos:**
1. Converter para script .py com tratamento de erros
2. Adicionar logging detalhado
3. Implementar verificação de inputs
4. Criar Dockerfile básico
5. Testar em ambiente isolado

O notebook atual já contém toda a lógica necessária - a conversão será principalmente uma reorganização do código com adição de boas práticas de engenharia de software.
