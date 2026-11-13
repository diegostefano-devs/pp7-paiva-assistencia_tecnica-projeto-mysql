def criar_cliente(cpf:str, nome, telefone:str):

    if not nome:
        raise ValueError("Campo obrigatorio")

    if not cpf:
        raise ValueError("Campo obrigatorio")

    if not telefone:
        raise ValueError("Campo obrigatorio")

    if len(cpf) != 14 or not cpf.isdigit:
        raise ValueError("Formato de CPF inválido.")
    
    if len(telefone) != 14 or not telefone.isdigit:
        raise ValueError("Formato de número de telefone inválido.")
        

    return {
        "cpf" : cpf,
        "nome" : nome,
        "telefone" : telefone
    }