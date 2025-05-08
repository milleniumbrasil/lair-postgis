#!/bin/bash

# Configurar variáveis de ambiente padrão se não estiverem definidas
export INPUT_PATH=${INPUT_PATH:-"/home/jovyan/data/input"}
export OUTPUT_PATH=${OUTPUT_PATH:-"/home/jovyan/data/output"}

# Verificar se os diretórios existem
mkdir -p "$INPUT_PATH" "$OUTPUT_PATH"

echo "🔧 Configuração:"
echo "- INPUT_PATH: $INPUT_PATH"
echo "- OUTPUT_PATH: $OUTPUT_PATH"

# Primeiro rodar o script de substituição dos inputs
echo "🔄 Substituindo chamadas de input() nos notebooks..."
cd /home/jovyan/work
python patch_notebooks_inputs.py

NOTEBOOKS=(
  "01_Download_CAR_estados.ipynb"
  "02_UsosABC.ipynb"
  "03_Declividade.ipynb"
  "04_CorrecaoEdafo.ipynb"
  "05_AptdEdafo.ipynb"
  "06_TerraIndigena.ipynb"
  "07_AmazoniaLegal.ipynb"
  "08_FaixaFronteira.ipynb"
  "09_UCPI.ipynb"
  "10_IntegracoesCAR.ipynb"
  "11_AdequarParaBancoDados.ipynb"
  "12_To_PostGis.ipynb"
)

# Criar diretório para saída
mkdir -p /home/jovyan/work/notebooks/output

for nb in "${NOTEBOOKS[@]}"; do
  echo "📓 Executando $nb..."
  # Verificar se o notebook existe
  if [ -f "/home/jovyan/work/notebooks/$nb" ]; then
    papermill "/home/jovyan/work/notebooks/$nb" "/home/jovyan/work/notebooks/output/$nb" --log-output || echo "⚠️ Erro ao executar $nb"
  else
    echo "⚠️ Notebook não encontrado: /home/jovyan/work/notebooks/$nb"
  fi
done

echo "✅ Todos os notebooks foram executados!"