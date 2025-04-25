#!/bin/bash
set -e
# Build standalone executable for lair-postgis using PyInstaller
# Use isolated virtual environment to avoid system package installation issues
BUILD_ENV=".build-env"
if [ ! -d "$BUILD_ENV" ]; then
    python3 -m venv "$BUILD_ENV"
fi
source "$BUILD_ENV/bin/activate"
# Upgrade pip, setuptools, wheel and install PyInstaller (allow system packages override)
# Attempt install; if offline or protected env, skip and proceed
pip install --break-system-packages --upgrade pip setuptools wheel pyinstaller || \
echo "⚠️  Aviso: falha ao instalar dependências; prosseguindo com o ambiente existente"
## Build the standalone executable using venv PyInstaller, fallback to host if needed
if ! python -m PyInstaller --clean --onefile --name lair-postgis src/lair_postgis/cli.py; then
    echo "⚠️  PyInstaller não encontrado no venv; tentando 'pyinstaller' do sistema"
    pyinstaller --clean --onefile --name lair-postgis src/lair_postgis/cli.py
fi
deactivate