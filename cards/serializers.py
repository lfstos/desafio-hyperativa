from rest_framework import serializers
from .models import Cartao, Lote


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = '__all__'


class LoteSerializer(serializers.ModelSerializer):
    arquivo = serializers.FileField(write_only=True)

    class Meta:
        model = Lote
        fields = '__all__'