# Task: Habilitar execução do CLI `lair-postgis` via instalação com `pip`

## Objetivo

Permitir que o projeto `lair-postgis` seja instalado via `pip install lair-postgis` e que o comando `lair-postgis` fique disponível globalmente no terminal do sistema operacional (Linux, macOS, Windows). Após a instalação, o usuário deve ser capaz de executar o comando:

```bash
lair-postgis --help

de qualquer lugar do sistema.

⸻

Motivação

Atualmente, o projeto está configurado para execução local com poetry install, mas a instalação via pip ainda não disponibiliza o comando lair-postgis no terminal. Isso se deve à ausência da definição de ponto de entrada (entry_points) no arquivo pyproject.toml.

⸻

Arquivo a ser alterado
	•	pyproject.toml

⸻

Local exato da alteração

Adicionar ou completar a seção [tool.poetry.scripts] ao final do bloco [tool.poetry] já existente no pyproject.toml.

⸻

Instruções detalhadas
	1.	Localize o arquivo pyproject.toml na raiz do projeto.
	2.	Verifique se existe uma seção [tool.poetry.scripts]. Caso não exista, crie essa seção após o bloco [tool.poetry] ou antes de [tool.poetry.dependencies].
	3.	Adicione a seguinte linha de definição de script:

[tool.poetry.scripts]
lair-postgis = "lair_postgis.cli:main"

Isso pressupõe que o projeto contém um módulo lair_postgis/cli.py com uma função main() definida. Caso esteja em outro lugar, adapte o path do módulo conforme necessário.

⸻

Critérios de aceite
	•	Após a execução do comando poetry install ou pip install ., o binário lair-postgis deve estar disponível no terminal.
	•	O comando lair-postgis --help deve exibir a interface de ajuda esperada.
	•	A alteração deve preservar a compatibilidade com poetry build e poetry publish.

⸻

Como chegamos a essa solução

O projeto possui documentação e estrutura que sugerem a intenção de uso como ferramenta CLI global, mas faltava a definição de entry_points que é o mecanismo oficial do Python para registrar comandos executáveis. A instrução foi baseada em boas práticas para distribuição de pacotes Python no PyPI com suporte multiplataforma.

⸻

Observação final

Após essa alteração, recomenda-se executar:

poetry build
pip install dist/lair_postgis-*.whl
lair-postgis --help

para validar o funcionamento antes de publicar com:

poetry publish --build

--- 
