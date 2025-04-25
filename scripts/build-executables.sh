#!/bin/bash
set -e
# Build standalone executable for lair-postgis using PyInstaller
# Install PyInstaller via the default Python interpreter
python -m pip install pyinstaller
# Invoke PyInstaller as a Python module to ensure correct environment
python -m PyInstaller --clean --onefile --name lair-postgis src/lair_postgis/cli.py