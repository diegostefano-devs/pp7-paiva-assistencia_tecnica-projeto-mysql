from models.tecnico_models import criar_tecnico
from repositories.tecnico_repositories import cadastrar, listar_tecnico
from repositories.cliente_repository import  validar_cpf, excluir, alterar


def cadastrar_tecnico(cpf, nome, telefone):
    tecnico = criar_tecnico(cpf, nome, telefone)

    if tecnico is None:
        print("Dados inválidos!")
        return False

    if validar_cpf(cpf):
        print("Este CPF já consta no sistema.")

    resultado = cadastrar(tecnico)

    if resultado:
        print("Técnico cadastrado com sucesso.")
        return True

    print("Não foi possivel cadastrar técnico")
    return False



def tecnico():
    tecnico = listar_tecnico()

    if not tecnico:
        return None
    
    return tecnico


def excluir_tecnico(cpf):

    if validar_cpf(cpf):
        return excluir(cpf)

    print("CPF não consta no banco de dados.")
    return False

def atualizar_tecnico(nome, telefone, cpf):
    if validar_cpf(cpf):
        return alterar(nome, telefone, cpf)

    print("CPF não consta no banco de dados.")
    return
