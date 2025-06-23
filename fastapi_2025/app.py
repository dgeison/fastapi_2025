from http import HTTPStatus

from fastapi import FastAPI

from fastapi_2025.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()


database = []  # provisionar um banco de dados simples para testes


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Welcome to the FastAPI application!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    """
    Cria um novo usuário.

    Este endpoint recebe um objeto `UserSchema`
    contendo os detalhes do usuário
    e retorna uma mensagem de confirmação.
    """
    # breakpoint()

    # Simula a criação de um usuário no banco de dados
    # Aqui, estamos apenas adicionando o usuário a uma lista em memória
    # Em uma aplicação real, você usaria um ORM ou uma conexão com o
    # banco de dados
    #
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    # user_with_id = UserDB(
    #     id=len(database) + 1,
    #     username=user.username,
    #     email=user.email,
    #     password=user.password,
    # )

    database.append(user_with_id)
    return user_with_id
