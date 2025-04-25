# lair-postgis
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
