def criar_tecnico(cpf: str, nome: str, telefone: str):
    if len(cpf) != 14:
        raise ValueError("Formato de CPF inválido. Use o padrão 000.000.000-00.")

    if len(telefone) < 10 or len(telefone) > 15:
        raise ValueError("Formato de número de telefone inválido.")

    return {
        'cpf': cpf,
        'nome': nome,
        'telefone': telefone
    }

