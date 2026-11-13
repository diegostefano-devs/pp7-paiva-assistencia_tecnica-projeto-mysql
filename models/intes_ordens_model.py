def criar_itens_os (id_os, id_peca, quantidade, preco_uni):

    if not id_os or not id_peca or not quantidade or not preco_uni:
        raise ValueError ("Todos os campos são obrigatórios.")
    if quantidade <= 0 or preco_uni <= 0:
        raise ValueError ("Coloque um valor válido.")

    return {
        "id_os" : id_os,
        "id_peca" : id_peca,
        "quantidade" : quantidade,
        "preco_uni" : preco_uni
    }