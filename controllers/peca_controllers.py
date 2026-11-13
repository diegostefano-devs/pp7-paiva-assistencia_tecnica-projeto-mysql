from models.peca_model import criar_peca
from repositories.peca_repository import cadastrar_peca_db, listar_peca, excluir_peca, alterar_peca

def cadastrar_peca(nome, categoria, quantidade, estado, preco):

    if not nome or not nome.strip() or not categoria or not categoria.strip():
        raise ValueError("Campos obrigatórios!")

    peca = criar_peca(nome, categoria, quantidade, estado, preco)
    if peca is None:
        raise ValueError("Dados inválidos!")

    correto = cadastrar_peca_db(peca)

    if not correto:
        raise ValueError("Erro: Não foi possível cadastrar peça!")
    return True



def atualizar_peca(peca_id, nome, categoria, quantidade, estado, preco):
    if not peca_id:
        raise ValueError("Campo obrigatório para atualização!")

    if not nome or not nome.strip() or not categoria or not categoria.strip():
        raise ValueError("Campo obrigatório!")

    correto = alterar_peca(peca_id, nome, categoria, quantidade, estado, preco)

    if not correto:
        raise ValueError("Erro: Não foi possível atualizar peças!")
    