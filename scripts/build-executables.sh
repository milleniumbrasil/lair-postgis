#!/bin/bash
set -e
# Build standalone executable for lair-postgis using PyInstaller
pip install pyinstaller
# Ensure PyInstaller is invoked via Python module to locate it correctly
python3 -m PyInstaller --clean --onefile --name lair-postgis src/lair_postgis/cli.py