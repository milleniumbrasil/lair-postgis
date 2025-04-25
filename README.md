# lair-postgis
 
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen)](https://milleniumbrasil.github.io/lair-postgis/) [![Build Binaries](https://img.shields.io/github/v/release/milleniumbrasil/lair-postgis?label=binaries)](https://github.com/milleniumbrasil/lair-postgis/releases) [![GitHub Actions CI](https://github.com/milleniumbrasil/lair-postgis/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/milleniumbrasil/lair-postgis/actions)

Ferramenta CLI para scaffolding de projetos PostGIS com Docker e scripts de inicialização.

## Instalação via Python (usuários avançados)

```bash
pip install lair-postgis
```

> Esta opção é indicada para desenvolvedores ou usuários que já possuem o ambiente Python configurado.

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

## Executando binários não assinados

### Windows

Ao tentar executar `lair-postgis.exe`, o Windows pode exibir um alerta de segurança do SmartScreen.

#### Como prosseguir:
1. Clique em **"Mais informações"**.
2. Clique em **"Executar assim mesmo"**.
3. O aplicativo será iniciado normalmente.

Essa mensagem ocorre porque o binário não é assinado digitalmente. Isso **não indica que o programa é malicioso**.

### macOS

O sistema pode mostrar:

> “lair-postgis” não pode ser aberto porque o desenvolvedor não pode ser verificado.

#### Como permitir a execução:
```bash
xattr -d com.apple.quarantine ./lair-postgis
chmod +x ./lair-postgis
sudo mv ./lair-postgis /usr/local/bin/
```

Agora, você pode executar normalmente com:
```bash
lair-postgis --help
```

### Linux

```bash
chmod +x ./lair-postgis
./lair-postgis --help

# Para tornar o comando global:
sudo mv ./lair-postgis /usr/local/bin/
``` 
