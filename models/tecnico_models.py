def criar_tecnico(cpf:str, nome: str, telefone:str):
    if cpf != 14 or not cpf.isdigt:
        print("Formato de CPF inválido.")
        return None
    

    if telefone != 14 or not telefone.isdigt:
            print("Formato de número de telefone inválido.")
            return None


    return {
         'cpf': cpf,
         'nome': nome,
         'telefone': telefone
    }
