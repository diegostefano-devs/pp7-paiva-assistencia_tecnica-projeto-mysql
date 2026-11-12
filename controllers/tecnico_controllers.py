from models.tecnico_models import criar_tecnico
from repositories.tecnico_repositories import (
    cadastrar,
    listar_tecnico,
    validar_cpf,
    excluir,
    alterar
)

def cadastrar_tecnico(cpf, nome, telefone):
    if not nome or not nome.strip() or not cpf or not cpf.strip():
        raise ValueError("Nome e CPF são obrigatórios!")
    if validar_cpf(cpf):
        raise ValueError("Este CPF já consta no sistema.")        
    tecnico = criar_tecnico(cpf, nome, telefone)

    
    if tecnico is None:
        raise ValueError("Dados invalidos")


    sucesso = cadastrar(tecnico)

    if not sucesso:
        raise Exception("Não foi possível cadastrar o técnico no banco de dados.")
    return True



def tecnico():
    tecnico = listar_tecnico()
    return tecnico if tecnico else []


def excluir_tecnico(cpf):
    if not cpf or not cpf.strip():
        raise ValueError("Informe o CPF para excluir.")
    if not validar_cpf(cpf):
        raise ValueError("CPF não consta no banco de dados.")

    sucesso = excluir(cpf)
    if not sucesso:
        raise Exception("Erro ao excluir o técnico.")
    return True

def atualizar_tecnico(nome, telefone, cpf):
    if not cpf or not cpf.strip():
        raise ValueError("CPF é obrigatório para atualização.")
    if not validar_cpf(cpf):
        raise ValueError("CPF não consta no banco de dados.")
    if not nome or not nome.strip():
        raise ValueError("O campo 'Nome' não pode ficar vazio.")

    sucesso = alterar(nome, telefone, cpf)
    if not sucesso:
        raise Exception("Erro ao atualizar o técnico.")
    return True