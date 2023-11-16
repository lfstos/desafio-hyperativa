import logging
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Lote, Cartao
from .serializers import LoteSerializer, CartaoSerializer

logger = logging.getLogger(__name__)


class CartaoListCreateView(generics.ListCreateAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    permission_classes = [IsAuthenticated]


class ConsultarCartaoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, numero_cartao):
        try:
            cartao = Cartao.objects.get(numero_cartao=numero_cartao)
            return Response({'identificador_sistema': cartao.id})
        except Cartao.DoesNotExist:
            return Response({'error': 'Cartão não encontrado'}, status=status.HTTP_404_NOT_FOUND)


class LoteListCreateView(generics.ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer