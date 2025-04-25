# lair-postgis

## Sumário

Esta documentação está organizada da seguinte forma:

- [Instalação via Python (usuários avançados)](#instalacao-via-python-usuarios-avancados): Instalação via pip para usuários com Python.
- [Interface de Linha de Comando](#interface-de-linha-de-comando): Opções disponíveis, flags e códigos de saída.
- [Exemplos](#exemplos): Exemplos de uso do comando e estrutura gerada.
- [Executando binários não assinados](#executando-binarios-nao-assinados): Instruções para executar binários sem assinatura.

---

## Instalação via Python (usuários avançados)

```bash
pip install lair-postgis
```

> Esta opção é indicada para desenvolvedores ou usuários que já possuem o ambiente Python configurado.

---

## Interface de Linha de Comando

```bash
lair-postgis --in caminho/para/lair.sql [--out caminho/para/install]
```

**Opções:**

| Flag           | Descrição                                                                           |
| -------------- | ----------------------------------------------------------------------------------- |
| `--in`         | Caminho para o arquivo `lair.sql` (obrigatório).                                     |
| `--out`        | Diretório de saída para a estrutura gerada (padrão: diretório atual).                |
| `--version`    | Exibe a versão do `lair-postgis`.                                                    |
| `-h`, `--help` | Exibe informações de ajuda.                                                         |

### Códigos de Saída

- `0`: Sucesso.
- `1`: Dependência ausente ou parâmetros inválidos.

---

## Exemplos

### Exemplo Básico

```bash
lair-postgis --in ./schema/lair.sql --out ./deploy
```

Isso criará:

```text
deploy/
├── Dockerfile
├── docker-compose.yml
└── init-db/
    ├── 01-init.sql
    └── 10-lair.sql
```

### Após o Scaffold

Para executar o banco de dados:

```bash
cd deploy
docker compose down -v && docker compose up --build -d
```

---

**Repositório:** https://github.com/milleniumbrasil/lair-postgis  
**Documentação:** https://milleniumbrasil.github.io/lair-postgis/  

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