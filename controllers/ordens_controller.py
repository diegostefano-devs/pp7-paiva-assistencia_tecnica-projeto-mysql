from models.ordens_model import criar_os
from repositories.ordens_repository import buscar_tec, abrir_os, validar_id_cliente, listar_os, listar_os_status, finalizar_os, validar_os

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

def finalizar_ordem_de_servico(ordem_id, status):
    try:
        validar_os(ordem_id)

        finalizar_os(ordem_id, status)
        print("Operação concluída!")
    except ValueError as observacao:
        print(f"Erro ao realizar operação: {observacao}")
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")

def listar_todas_os():
    try:
        resultado = listar_os()
        return resultado
    except ValueError as erro:
        print(f"Erro ao realizar operação: {erro}")

def listar_os_por_status(status):
    try:
        listar_os_status(status)
    except ValueError as erro:
        print(f"Erro ao realizar operação: {erro}")
