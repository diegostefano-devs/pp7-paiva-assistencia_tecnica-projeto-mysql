from models.cliente_model import criar_cliente
from repositories.cliente_repository import cadastrar, validar_cpf, listar_clientes, excluir, alterar, buscar_cliente

def cadastrar_cliente(cpf, nome, telefone):
    try:
        cliente = criar_cliente(cpf, nome, telefone)
        cadastrar(cliente)
        return True
    except ValueError as erro:
        print(f"Atenção: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")

def clientes():
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
        excluir(cpf)
        print("Sucesso: Cliente excluído com sucesso!")
    except ValueError as erro:
        print(f"Atenção: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    

def atualizar_cliente(nome, telefone, cpf):
    if not cpf or not cpf.strip():
        raise ValueError("CPF é obrigatório para atualização.")
    
    try:
        alterar(nome, telefone, cpf)
        print("Sucesso! Informações alteradas com êxito.")
    except ValueError as erro:
        print(f"Atenção: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
