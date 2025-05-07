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

## Requisitos

- Python 3.8 ou superior
- GDAL/OGR
- Tesseract OCR

## Instalação das Dependências

### 1. Instalar Python

Faça o download e instale o Python 3.8 ou superior do [site oficial](https://www.python.org/downloads/).

### 2. Instalar GDAL/OGR

#### Windows:
- Baixe as wheel do GDAL de: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
- Instale com pip: `pip install caminho/para/arquivo.whl`

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3-gdal gdal-bin libgdal-dev
```

#### macOS:
```bash
brew install gdal
```

### 3. Instalar Tesseract OCR

#### Windows:
- Baixe o instalador de: https://github.com/UB-Mannheim/tesseract/wiki
- Adicione o diretório de instalação ao PATH do sistema

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install tesseract-ocr
```

#### macOS:
```bash
brew install tesseract
```

### 4. Instalar Dependências Python

Na raiz do projeto, execute:

```bash
pip install -e .
```

Para instalar também as dependências de desenvolvimento:
```bash
pip install -e ".[dev]"
```

## Execução

### Executar Todos os Scripts em Sequência

```bash
python 00_Main.py
```

### Executar Scripts Individualmente

Você pode executar cada script individualmente:

```bash
python 01_Download_CAR_estados.py
```

## Observações Importantes

1. Ao executar os scripts, será solicitado o caminho para diversos diretórios e arquivos. Tenha essas informações preparadas.

2. Os scripts realizam a verificação de dependências e tentarão instalar automaticamente o que estiver faltando, mas algumas dependências (como GDAL e Tesseract) requerem instalação manual conforme as instruções acima.

3. Para o script 01, é necessário um email válido para acesso ao sistema SICAR.

4. Para o script 12, é necessário ter um servidor PostgreSQL em execução.

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