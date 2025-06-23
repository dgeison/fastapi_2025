from http import HTTPStatus


def test_read_root(client):
    """
    Testa se o endpoint raiz ("/") está funcionando corretamente.

    Verifica se a resposta tem o status HTTP 200 (OK) e se o corpo
    da resposta contém a mensagem de boas-vindas esperada.
    """
    # Arrange (Organizar):
    # Cria uma instância do cliente de teste para a aplicação.
    # client = TestClient(app)

    # Act (Agir):
    # Faz uma requisição GET para o endpoint raiz.
    response = client.get('/')

    # Assert (Verificar):
    # Confere se o código de status da resposta é 200 (OK)
    # e se o JSON da resposta corresponde à mensagem esperada.
    assert response.json() == {
        'message': 'Welcome to the FastAPI application!'
    }


def test_create_user(client):
    """
    Testa o endpoint de criação de usuário ("/users").

    Verifica se a criação de um usuário com dados válidos
    retorna o status HTTP 201 (Created) e se os dados do usuário
    retornados estão corretos.
    """
    # Arrange (Organizar):
    # client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret_alice',
        },
    )

    # Assert (Verificar):
    # Verifica se o código de status da resposta é 201 (Created)
    assert response.status_code == HTTPStatus.CREATED

    # Verifica se o JSON da resposta contém os dados do usuário criado
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }
