from django.db import models


class Lote(models.Model):
    lote = models.CharField(max_length=8)
    qtd_registros = models.IntegerField()


class Cartao(models.Model):
    identificador_linha = models.CharField(max_length=1)
    numeracao_lote = models.CharField(max_length=6)
    numero_cartao = models.CharField(max_length=18)
    lote = models.ForeignKey(Lote, on_delete=models.PROTECT)