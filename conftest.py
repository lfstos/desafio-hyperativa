import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

@pytest.fixture
def user_with_token(db):
    # Crie um usuário usando o mixer ou qualquer outra forma
    user = mixer.blend(get_user_model())

    # Cria um token de acesso para o usuário
    access_token = AccessToken.for_user(user)

    # Configura o token no cabeçalho de autorização do cliente
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    return user, client 