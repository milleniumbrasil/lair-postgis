# Task 03: Documentar contornos para execução de binários não assinados e incluir alternativas para usuários com Python

## Objetivo

Atualizar a documentação do projeto `lair-postgis` para incluir:

1. Instruções completas para executar binários standalone **sem assinatura digital** (Windows, macOS e Linux).
2. Alternativa clara para **usuários que preferem instalar via Python**, com instruções usando `pip`.
3. Correção das **badges do README.md** com base no estado atual do projeto.

---

## Justificativa

O projeto distribui binários standalone para facilitar a vida de usuários leigos, mas também deve suportar quem conhece Python e prefere instalar via `pip`. Além disso, as badges do `README.md` devem refletir corretamente o repositório, status da documentação e versão publicada.

---

## Alterações obrigatórias

### Arquivos a serem modificados:
- `README.md`
- `docs/index.md`

---

## Etapas da modificação

### 🔹 Etapa 1 – Instruções para execução de binários não assinados

Adicionar ao final de ambos os arquivos uma nova seção:

```markdown
## Executando binários não assinados
```

#### Incluir os seguintes blocos de instrução:

##### Windows

```markdown
### Windows

Ao tentar executar `lair-postgis.exe`, o Windows pode exibir um alerta de segurança do SmartScreen.

#### Como prosseguir:
1. Clique em **"Mais informações"**.
2. Clique em **"Executar assim mesmo"**.
3. O aplicativo será iniciado normalmente.

Essa mensagem ocorre porque o binário não é assinado digitalmente. Isso **não indica que o programa é malicioso**.
```

##### macOS

```markdown
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
```

##### Linux

```markdown
### Linux

```bash
chmod +x ./lair-postgis
./lair-postgis --help

# Para tornar o comando global:
sudo mv ./lair-postgis /usr/local/bin/
```
```

---

### 🔹 Etapa 2 – Alternativa para usuários com Python

Adicionar uma seção anterior à de binários:

```markdown
## Instalação via Python (usuários avançados)

Se você possui Python 3.9+ instalado, é possível instalar via pip:

```bash
pip install lair-postgis
```

Após a instalação, o comando ficará disponível no terminal:

```bash
lair-postgis --help
```

> Esta opção é indicada para desenvolvedores ou usuários que já possuem o ambiente Python configurado.
```

---

### 🔹 Etapa 3 – Verificação e correção das badges no README

Verificar no `README.md`:

```markdown
[![PyPI version](https://badge.fury.io/py/lair-postgis.svg)](https://badge.fury.io/py/lair-postgis)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen)](https://milleniumbrasil.github.io/lair-postgis/)
[![GitHub Actions CI](https://github.com/milleniumbrasil/lair-postgis/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/milleniumbrasil/lair-postgis/actions)
```

#### Corrigir conforme:

1. Verificar se o pacote `lair-postgis` realmente está publicado no [PyPI](https://pypi.org/project/lair-postgis/).
   - Se não estiver, **remover ou comentar** a badge do PyPI.
2. Verificar se o link de deploy da documentação está ativo no GitHub Pages.
   - Exemplo: [https://milleniumbrasil.github.io/lair-postgis](https://milleniumbrasil.github.io/lair-postgis)
3. Verificar o nome e localização corretos do workflow do GitHub Actions (`deploy-docs.yml`) para manter a badge funcional.

---

## Critérios de aceite

- A documentação final deve incluir:
  - Caminhos distintos para usuários leigos (binário) e usuários avançados (Python).
  - Instruções específicas para cada sistema operacional.
  - Badges funcionais e atualizados no `README.md`.
- O conteúdo deve estar disponível em:
  - `README.md`
  - `docs/index.md`
