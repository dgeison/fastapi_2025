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
