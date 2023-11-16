import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer  # Criando dados fictícios


@pytest.mark.django_db
def test_cartao_list_create_view_authenticated(client):
    # Crie um usuário usando o mixer ou qualquer outra forma
    user = mixer.blend(get_user_model())

    # Crie um token de acesso para o usuário
    access_token = AccessToken.for_user(user)

    # Configure o token no cabeçalho de autorização do cliente
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    # Agora você pode usar o cliente configurado nos seus testes
    response = client.get('/seu-endpoint-aqui/')

    # Faça asserções conforme necessário
    assert response.status_code == 200


@pytest.mark.django_db
def test_consultar_cartao_view_authenticated(client, user_with_token):
    user, client = user_with_token  # Obtendo o usuário e o cliente do fixture

    # Criando um cartão fictício para testar a consulta
    cartao = mixer.blend('cards.Cartao', numero_cartao='123456789012345678')

    url = reverse('consultar-cartao', args=[cartao.numero_cartao])

    # Use o cliente configurado com o token de acesso
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cartao_list_create_view_unauthenticated(client):
    url = reverse('cartao-list-create')
    response = client.post(url, {'identificador_linha': 'C1', 'numeracao_lote': '000001',
                           'numero_cartao': '123456789012345678'}, format='json')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
