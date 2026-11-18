from models.peca_model import criar_peca
from repositories.peca_repository import cadastrar_peca_db, listar_peca, excluir_peca, alterar_peca, buscar_peca

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

def mostrar_uma_peca(id_peca):
    if not id_peca:
        raise ValueError("Informe o ID da peça.")

    try:
        peca = buscar_peca(id_peca)
        if not peca:
            print("Peça não encontrada")
        return peca
    except ValueError as e:
        print(f"Atenção: {e}")
        return None

def deletar_peca(id_peca):
    try:
        if not id_peca:
            raise ValueError("Campo obrigatório para atualização!")

        teste = buscar_peca(id_peca)
        if not teste:
            raise ValueError ("Peça não cadastrada no banco de dados.")

        resultado = excluir_peca(id_peca)
        if resultado:
            print("Peça excluída com sucesso!")
        return resultado
    except ValueError as erro:
        print(f"Atenção: {erro}")
        raise
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        raise


def atualizar_peca(peca_id, nome, categoria, quantidade, estado, preco):
    try:
        if not peca_id:
            raise ValueError("Campo obrigatório para atualização!")

        if not nome or not nome.strip() or not categoria or not categoria.strip():
            raise ValueError("Campo obrigatório!")

        teste = buscar_peca(peca_id)
        if not teste:
            raise ValueError ("Peça não cadastrada no banco de dados.")
        
        correto = alterar_peca(peca_id, nome, categoria, quantidade, estado, preco)
        if correto:
            print("Peça alterada com sucesso!")
        return correto
    except ValueError as erro:
        print(f"Atenção: {erro}")
        raise
    except Exception as erro:
        print(f'Erro inesperado: {erro}')
        raise

    