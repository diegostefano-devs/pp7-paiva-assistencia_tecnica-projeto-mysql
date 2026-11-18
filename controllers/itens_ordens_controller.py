from repositories.itens_ordens_repository import add_itens_ordens, validar_os, validar_peca
from models.intes_ordens_model import criar_itens_os

def abrir_orcamento(id_os, id_peca, quantidade, valor_fixo):
    try:
        id_ordem = validar_os(id_os)

        peca_id = validar_peca(id_peca)

        itens_os = criar_itens_os(id_ordem, peca_id, quantidade)

        resultado = add_itens_ordens(itens_os, valor_fixo)
        print("Orçamento aplicado!")
        return resultado
    except ValueError as observacao:
        print(f"Erro de validação: {observacao}")
        raise
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")
        raise

