def criar_itens_os (id_os, id_peca, quantidade):

    if not id_os or not id_peca or not quantidade :
        raise ValueError ("Todos os campos são obrigatórios.")
    if int(quantidade) <= 0:
        raise ValueError ("Coloque um valor válido.")

    return {
        "id_os" : id_os,
        "id_peca" : id_peca,
        "quantidade" : quantidade    }