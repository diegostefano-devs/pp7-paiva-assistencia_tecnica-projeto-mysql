from models.cliente_model import criar_clinte
from repositories.cliente_repository import cadastrar, validar_cpf, listar_clientes, excluir, alterar

def cadastrar_cliente(cpf, nome, telefone):
    cliente = criar_clinte(cpf, nome, telefone)

    if cliente is None:
        print("Dados inválidos!")
        return False

    if validar_cpf(cpf):
        print("Este CPF já consta no sistema.")
        return

    resultado = cadastrar(cliente)

    if resultado:
        print("Cliente cadastrado com sucesso.")
        return True

    print("Não foi possível cadastrar cliente.")
    return False

def clientes():
    clientes = listar_clientes()

    if not clientes:
        return None
    return clientes

def excluir_cliente(cpf):
    if validar_cpf(cpf):
        return excluir(cpf)

    print("CPF não consta no banco de dados.")
    return False

def atualizar_cliente(nome, telefone, cpf):
    if validar_cpf(cpf):
        return alterar(nome, telefone, cpf)

    print("CPF não consta no banco de dados.")
    return
