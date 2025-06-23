import pytest
from fastapi.testclient import TestClient

from fastapi_2025.app import app


@pytest.fixture
def client():
    """
    Fixture para criar um cliente de teste para a aplicação FastAPI.

    Retorna uma instância do TestClient que pode ser usada
    para fazer requisições aos endpoints da aplicação.
    """
    return TestClient(app)
