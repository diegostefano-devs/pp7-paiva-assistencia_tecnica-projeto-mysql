from models.cliente_model import criar_clinete
from repositories.cliente_repository import cadastrar, validar_cpf, listar_clientes, excluir, alterar

def cadastrar_cliente(cpf, nome, telefone):
    if not nome or not nome.strip() or not cpf or not cpf.strip():
        raise ValueError("Nome e CPF são obrigatórios!")

    if validar_cpf(cpf):
        raise ValueError("Este CPF já consta no sistema.")

    cliente = criar_clinete(cpf, nome, telefone)
    if cliente is None:
        raise ValueError("Dados inválidos para o cliente.")

    sucesso = cadastrar(cliente)
    if not sucesso:
        raise Exception("Não foi possível cadastrar o cliente no banco de dados.")
    
    return True

def clientes():
    lista = listar_clientes()
    return lista if lista else []

def excluir_cliente(cpf):
    if not cpf or not cpf.strip():
        raise ValueError("Informe o CPF para excluir.")
    
    if not validar_cpf(cpf):
        raise ValueError("CPF não consta no banco de dados.")
    
    sucesso = excluir(cpf)
    if not sucesso:
        raise Exception("Erro ao excluir o cliente.")
    return True

def atualizar_cliente(nome, telefone, cpf):
    if not cpf or not cpf.strip():
        raise ValueError("CPF é obrigatório para atualização.")
    
    if not validar_cpf(cpf):
        raise ValueError("CPF não consta no banco de dados.")
    
    if not nome or not nome.strip():
        raise ValueError("O campo 'Nome' não pode ficar vazio.")

    sucesso = alterar(nome, telefone, cpf)
    if not sucesso:
        raise Exception("Erro ao atualizar o cliente.")
    return True
