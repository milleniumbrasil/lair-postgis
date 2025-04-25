# lair-postgis
[![PyPI version](https://badge.fury.io/py/lair-postgis.svg)](https://badge.fury.io/py/lair-postgis) [![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen)](https://milleniumbrasil.github.io/lair-postgis/) [![GitHub Actions CI](https://github.com/milleniumbrasil/lair-postgis/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/milleniumbrasil/lair-postgis/actions)
CLI tool to scaffold a PostGIS project with Docker, including init scripts.

## Prerequisites
- Docker (https://www.docker.com/get-started)
- CMake (e.g., `brew install cmake` on macOS or `sudo apt-get install cmake` on Debian/Ubuntu)

## Installation
```bash
poetry install
```

## Usage
```bash
lair-postgis --in path/to/lair.sql [--out path/to/install]
```

## Next Steps
After scaffolding, run:
```bash
cd path/to/install
docker compose down -v && docker compose up --build -d
```
