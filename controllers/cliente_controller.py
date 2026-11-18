from models.cliente_model import criar_cliente
from repositories.cliente_repository import cadastrar, validar_cpf, listar_clientes, excluir, alterar, buscar_cliente

def cadastrar_cliente(cpf, nome, telefone):
    try:
        cliente = criar_cliente(cpf, nome, telefone)
        resultado = cadastrar(cliente)
        return resultado    
    except ValueError as erro:
        print(f"Atenção: {erro}")
        raise
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        raise

def mostrar_clientes():
    lista = listar_clientes()
    return lista if lista else []

def mostrar_um_cliente(id_cliente):
    if not id_cliente:
        raise ValueError("Informe o CPF para excluir.")
    
    try:
        cliente = buscar_cliente(id_cliente)
        if not cliente:
            print("Cliente não encontrado.")
        return cliente
    except ValueError as erro:
        print(f"Atenção: {erro}")
        return None

def excluir_cliente(cpf):
    if not cpf or not cpf.strip():
        raise ValueError("Informe o CPF para excluir.")

    try:
        resultado = excluir(cpf)
        print("Sucesso: Cliente excluído com sucesso!")
        return resultado
    except ValueError as erro:
        print(f"Atenção: {erro}")
        raise
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        raise

    

def atualizar_cliente(nome, telefone, cpf):
    try:
        if not cpf or not cpf.strip():
            raise ValueError("CPF é obrigatório para atualização.")

        teste = buscar_cliente(cpf)
        if not teste:
            raise ValueError("Cliente não cadastrado no banco de dados.")
        
        resultado = alterar(nome, telefone, cpf)
        if resultado:
            print("Sucesso! Informações alteradas com êxito.")
        return resultado
    except ValueError as erro:
        print(f"Atenção: {erro}")
        raise
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        raise
