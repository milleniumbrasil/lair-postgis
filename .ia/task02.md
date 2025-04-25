# Task: Gerar e publicar executáveis standalone do `lair-postgis` para Windows e macOS no GitHub Releases

## Objetivo

Transformar o projeto Python `lair-postgis` em um conjunto de binários standalone (`lair-postgis.exe` para Windows e `lair-postgis` para macOS/Linux), sem necessidade de Python instalado no sistema do usuário final.

Os binários devem ser automaticamente gerados e enviados ao GitHub Releases usando GitHub Actions.

---

## Justificativa

Usuários finais não devem precisar instalar Python, `pip` ou `poetry`. O comando `lair-postgis` deve estar disponível no terminal após o usuário baixar e colocar o binário no PATH.

---

## Pré-requisitos para execução desta task

Instalar localmente:
```bash
pip install pyinstaller
```

No ambiente de CI (GitHub Actions), adicionar isso via `requirements-build.txt` ou diretamente no workflow.

---

## Estrutura esperada do projeto

```
lair-postgis/
├── lair_postgis/
│   ├── __init__.py
│   └── cli.py          # Deve conter a função main()
├── pyproject.toml
├── README.md
├── Dockerfile
├── docker-compose.yaml
├── init-db/
│   └── ...
└── build/
    └── dist/           # PyInstaller output (será gerado)
```

---

## Etapas da modificação

### 🔹 Etapa 1 – Verificar função `main()`

No arquivo `lair_postgis/cli.py`, confirme se existe uma função `main()` executável, como:

```python
def main():
    import argparse
    ...
```

Caso não exista, crie uma função `main()` que seja o ponto de entrada da ferramenta.

---

### 🔹 Etapa 2 – Adicionar `pyinstaller.spec` personalizado

Criar um arquivo `build/lair-postgis.spec` com o seguinte conteúdo:

```python
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(
    ['lair_postgis/cli.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='lair-postgis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='lair-postgis'
)
```

---

### 🔹 Etapa 3 – Script de build local

Criar `scripts/build-executables.sh`:

```bash
#!/bin/bash
set -e
pip install pyinstaller
pyinstaller --clean --onefile --name lair-postgis lair_postgis/cli.py
```

Tornar executável:

```bash
chmod +x scripts/build-executables.sh
```

---

### 🔹 Etapa 4 – Adicionar workflow GitHub Actions

Criar ou editar `.github/workflows/build-binaries.yml`:

```yaml
name: Build and Release CLI Executables

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]

    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install PyInstaller
        run: pip install pyinstaller

      - name: Build executable
        run: |
          pyinstaller --clean --onefile --name lair-postgis lair_postgis/cli.py

      - name: Upload to release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            dist/lair-postgis*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

### 🔹 Etapa 5 – Atualizar o `README.md`

Substituir o conteúdo do arquivo `README.md` por:

[🔽 Ver conteúdo atualizado do README.md na resposta anterior.]

---

### 🔹 Etapa 6 – Assinatura de binários

A assinatura digital é opcional neste momento. Os binários podem ser distribuídos **sem assinatura** e os usuários poderão executar com:

- **Windows**: clicar em “Executar assim mesmo” na tela de alerta do SmartScreen.
- **macOS**: rodar no terminal:

```bash
xattr -d com.apple.quarantine ./lair-postgis
```

---

## Ponto de confirmação necessário

- [x] O ponto de entrada é `lair_postgis/cli.py` com função `main()`
- [x] O nome do binário deve ser `lair-postgis`
- [x] Assinatura digital será omitida por enquanto, sem impacto para uso interno

---

## Critérios de aceite

- Após `git tag vX.Y.Z && git push --tags`, o GitHub deve gerar um release contendo:
  - `lair-postgis.exe` (Windows)
  - `lair-postgis` (macOS e Linux)
- O binário deve rodar com `--help` sem Python instalado no sistema.
