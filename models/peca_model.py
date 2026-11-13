def criar_peca(nome: str, categoria: str, quantidade: int, estado: str, preco: float):

    if not nome or not nome.strip():
        raise ValueError("Campo obrigatório!")

    if not categoria or not categoria.strip():
            raise ValueError("Campo obrigatório!")

    try:
        qtd = int(quantidade)
        if qtd < 0:
            print("A quantidade não pode ser negativa!")
            return None
    except ValueError:
        print("Quantidade inválida.")
        return None

    estado_limpo = estado.strip() if estado else ""
    if len(estado_limpo) > 10:
        print("O estado deve ter no máximo 10 caracteres.")
        return None

    try:
        prc = float(preco)
        if prc < 0:
            print("O preço não pode ser negativo!")
            return None
    except ValueError:
        print("Preço inválido.")
        return None

    return {
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'estado': estado,
        'preco': preco
    }