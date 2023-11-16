from .models import Lote, Cartao

def processar_arquivo(arquivo_path):
    with open(arquivo_path, 'r') as arquivo:
        linhas = arquivo.readlines()

        # Processar informações do lote
        info_lote = linhas[0].split()
        lote = info_lote[0]
        qtd_registros = info_lote[1]
        novo_lote = Lote.objects.create(lote=lote, qtd_registros=qtd_registros)

        # Processar informações dos cartões
        for linha in linhas[1:-1]:
            identificador_linha = linha[0]
            numeracao_lote = linha[1:7]
            numero_cartao = linha[7:26]

            Cartao.objects.create(
                identificador_linha=identificador_linha,
                numeracao_lote=numeracao_lote,
                numero_cartao=numero_cartao,
                lote=novo_lote,
            )