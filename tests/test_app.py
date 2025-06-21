from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_2025.app import app


def test_read_root():
    """
    Testa se o endpoint raiz ("/") está funcionando corretamente.

    Verifica se a resposta tem o status HTTP 200 (OK) e se o corpo
    da resposta contém a mensagem de boas-vindas esperada.
    """
    # Arrange (Organizar): Cria uma instância do cliente de teste para a aplicação.
    client = TestClient(app)

    # Act (Agir): Faz uma requisição GET para o endpoint raiz.
    response = client.get('/')

    # Assert (Verificar): Confere se o código de status da resposta é 200 (OK)
    # e se o JSON da resposta corresponde à mensagem esperada.
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Welcome to the FastAPI application!'
    }
