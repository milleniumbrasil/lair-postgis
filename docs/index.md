# lair-postgis

## Sumário

Esta documentação está organizada da seguinte forma:

- [Instalação](#instalacao): Como instalar e começar a usar o lair-postgis.
- [Interface de Linha de Comando](#interface-de-linha-de-comando): Opções disponíveis, flags e códigos de saída.
- [Exemplos](#exemplos): Exemplos de uso do comando e estrutura gerada.

---

## Instalação

```bash
pip install lair-postgis
```

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