def criar_clinte(cpf:str, nome, telefone:str):

    if cpf != 14 or not cpf.isdigit :
        print("Formato de CPF inválido.")
        return None
    
    if telefone != 14 or not telefone.isdigit:
        print("Formato de número de telefone inválido.")
        return None

    return {
        "cpf" : cpf,
        "nome" : nome,
        "telefone" : telefone
    }