#!/bin/bash

NOTEBOOKS=(
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

for nb in "${NOTEBOOKS[@]}"; do
  echo "Executando $nb..."
  papermill "notebooks/$nb" "notebooks/output/$nb"
done