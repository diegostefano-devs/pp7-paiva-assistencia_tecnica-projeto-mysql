from models.ordens_model import criar_os
from repositories.ordens_repository import buscar_tec, abrir_os, validar_id_cliente

def abrir_ordem(id_cliente, aparelho, problema):
    try:
        id_do_cliente = validar_id_cliente(id_cliente)

        dados_os = criar_os(id_do_cliente, aparelho, problema)

        id_tecnico = buscar_tec()

        resultado = abrir_os(dados_os, id_tecnico)

        print("OS aberta com sucesso!")
        return resultado
    except ValueError as ponto:
        print(f"Erro de validação: {ponto}")
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")
    