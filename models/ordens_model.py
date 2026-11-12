def abrir_os(id_cliente, aparelho, problema):

    if not id_cliente or not aparelho or not problema:
        raise ValueError("Todos os campos devem ser preenchidos.")

    return {
        "id_cliente" : id_cliente,
        "aparelho" : aparelho,
        "problema" : problema
    }