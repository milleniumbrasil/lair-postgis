# lair-postgis

[![PyPI version](https://badge.fury.io/py/lair-postgis.svg)](https://badge.fury.io/py/lair-postgis) [![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen)](https://milleniumbrasil.github.io/lair-postgis/) [![Build Binaries](https://img.shields.io/github/v/release/milleniumbrasil/lair-postgis?label=binaries)](https://github.com/milleniumbrasil/lair-postgis/releases) [![GitHub Actions CI](https://github.com/milleniumbrasil/lair-postgis/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/milleniumbrasil/lair-postgis/actions)

Ferramenta CLI para scaffolding de projetos PostGIS com Docker e scripts de inicialização.

## Instalação via pip

```bash
pip install lair-postgis
```

Após a instalação, execute:

```bash
lair-postgis --help
```

## Binaries Standalone

Para usuários sem Python instalado, disponibilizamos binários nos GitHub Releases:

- **Windows** (`.exe`): https://github.com/milleniumbrasil/lair-postgis/releases/latest/download/lair-postgis.exe
- **macOS/Linux**: https://github.com/milleniumbrasil/lair-postgis/releases/latest/download/lair-postgis

Basta baixar o executável e executá-lo diretamente:

```bash
./lair-postgis --help
```

## Build Local

Pré-requisitos:

```bash
pip install pyinstaller
```

Construir localmente:

```bash
chmod +x scripts/build-executables.sh
./scripts/build-executables.sh
```

O binário será gerado em `dist/lair-postgis` (macOS/Linux) ou `dist/lair-postgis.exe` (Windows).

## Uso

```bash
lair-postgis --in caminho/para/lair.sql [--out caminho/para/install]
```

## Documentação

https://milleniumbrasil.github.io/lair-postgis/

## Contribuição

Contribuições são bem-vindas! Faça um fork e envie pull requests.

## Licença

MIT © milleniumbrasil
