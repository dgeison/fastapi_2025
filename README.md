# FastAPI 2025

Projeto backend em Python utilizando FastAPI, com gerenciamento de dependências via Poetry e ferramentas auxiliares para desenvolvimento ágil.

---

## Visão Geral

Este projeto tem como objetivo servir de base para aplicações backend modernas utilizando FastAPI, com foco em organização, documentação e boas práticas de desenvolvimento.

---

## Estrutura Inicial do Projeto

```
fastapi_2025/
├── fastapi_2025/
│   └── app.py
├── tests/
├── pyproject.toml
└── README.md
```

---

## Ferramentas Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **FastAPI**: Framework web moderno e rápido.
- **Poetry**: Gerenciamento de dependências e ambiente virtual.
- **pipx**: Instalação isolada de ferramentas Python.
- **tree**: Visualização da estrutura de diretórios.

---

## Gerenciamento de Ambientes e Dependências

- **pipx**: Utilizado para instalar e isolar ferramentas Python globalmente, sem afetar o ambiente do sistema.
- **poetry**: Utilizado para gerenciamento de dependências, empacotamento e scripts do projeto.

---

## Ferramentas Auxiliares

- **tree**: Utilizada para exibir a estrutura de diretórios do projeto de forma hierárquica no terminal.

**Instalação no Linux:**
```sh
sudo apt install tree
```

**Uso:**
```sh
tree
```

---

## Inicialização do Projeto

O projeto foi criado usando o Poetry com o comando:
```sh
poetry new fastapi_2025
```

---

## Comandos Iniciais

- Ativar o ambiente Poetry:
  ```sh
  poetry shell
  ```
- Rodar o servidor FastAPI em modo desenvolvimento:
  ```sh
  fastapi dev fastapi_2025/app.py
  ```
  ou
  ```sh
  poetry run fastapi dev fastapi_2025/app.py
  ```

---

## Primeiro Endpoint

Arquivo: `fastapi_2025/app.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
```

---

## Boas Práticas e Qualidade de Código

O projeto utiliza ferramentas para garantir padronização, qualidade e automação:

- **ruff**: Lint e formatação de código Python.
- **pytest** e **pytest-cov**: Testes automatizados e relatório de cobertura.
- **taskipy**: Automatização de tarefas comuns do projeto.

### Ruff

O Ruff está configurado para aplicar as seguintes regras (seletores):

- **I**: Organização de imports (isort)
- **F**: Pyflakes (erros comuns)
- **E**: Erros de estilo (pycodestyle)
- **W**: Avisos de estilo (pycodestyle)
- **PL**: Pylint (boas práticas)
- **PT**: Pytest (boas práticas para testes)

Principais comandos:
```sh
poetry run ruff check .
poetry run ruff format .
```

### Testes Automatizados

- Para rodar todos os testes:
  ```sh
  poetry run pytest
  ```
- Para rodar os testes com relatório de cobertura e saída detalhada:
  ```sh
  poetry run pytest --cov=fastapi_2025 -v
  ```

- Para gerar relatório de cobertura em HTML:
  ```sh
  poetry run coverage html
  ```
  O relatório será salvo na pasta `htmlcov`. Abra `htmlcov/index.html` no navegador.

### Automatização de Tarefas com Taskipy

Tarefas configuradas no `pyproject.toml`:

- **lint**: `poetry run task lint` — Lint no código.
- **pre_format**: `poetry run task pre_format` — Corrige problemas simples de lint.
- **format**: `poetry run task format` — Formata o código.
- **run**: `poetry run task run` — Sobe o servidor FastAPI.
- **test**: `poetry run task test` — Executa lint, testes e gera cobertura HTML automaticamente.

---

## Testes de API

Exemplo de teste para o endpoint raiz:

Arquivo: `tests/test_app.py`

```python
from http import HTTPStatus
from fastapi.testclient import TestClient
from fastapi_2025.app import app

def test_read_root():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Welcome to the FastAPI application!'
    }
```

---


