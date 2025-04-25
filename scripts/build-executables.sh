#!/bin/bash
set -e
# Build standalone executable for lair-postgis using PyInstaller
pip install pyinstaller
pyinstaller --clean --onefile --name lair-postgis src/lair_postgis/cli.py