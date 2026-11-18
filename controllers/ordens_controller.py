from models.ordens_model import criar_os
from repositories.ordens_repository import buscar_tec, abrir_os, validar_id_cliente, listar_os, listar_os_status, finalizar_os, validar_os, buscar_os

def abrir_ordem(id_cliente, aparelho, problema):
    try:
        id_do_cliente = validar_id_cliente(id_cliente)
        if isinstance(id_do_cliente, tuple):
            id_do_cliente = id_do_cliente[0]

        dados_os = criar_os(id_do_cliente, aparelho, problema)

        id_tecnico = buscar_tec()

        resultado = abrir_os(dados_os, id_tecnico)

        print("OS aberta com sucesso!")
        return resultado
    except ValueError as ponto:
        print(f"Erro de validação: {ponto}")
        raise
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")
        raise


def aprovar_ordem_de_servico(ordem_id, status):
    try:
        teste = buscar_os(ordem_id)

        if not teste:
            raise ValueError(f"OS não encontrada no banco de dados.")

        if teste['status'] != "AGUARDANDO APROVAÇÃO":
            raise ValueError (f"Orçamento ainda não foi aplicado ou essa OS já está finalizada.") 

        resultado = finalizar_os(ordem_id, status)
        if resultado:
            print("Operação Concluída.")
        return resultado
    except ValueError as observacao:
        print(f"Erro ao realizar operação: {observacao}")
        raise
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")
        raise

def encerrar_ordem_servico(ordem_id, status):
    try:
        teste = buscar_os(ordem_id)

        if not teste:
            raise ValueError(f"OS não encontrada no banco de dados.")

        if teste['status'] != "EM MANUTENÇÃO.":
            raise ValueError (f"Essa OS ainda não foi iniciada ou já foi finalizada.") 

        resultado = finalizar_os(ordem_id, status)
        if resultado:
            print("Operação Concluída.")
        return resultado
    except ValueError as observacao:
        print(f"Erro ao realizar operação: {observacao}")
        raise
    except Exception as erro:
        print(f"Erro ao abrir OS no banco: {erro}")
        raise


def listar_todas_os():
    try:
        resultado = listar_os()
        return resultado
    except ValueError as erro:
        print(f"Erro ao realizar operação: {erro}")

def listar_os_por_status(status):
    try:
        resultado = listar_os_status(status)
        return resultado
    except ValueError as erro:
        print(f"Erro ao realizar operação: {erro}")
        return[]

def mostrar_uma_os(id_os):
    if not id_os:
        raise ValueError("Informe o ID da OS.")

    try: 
        ordem = buscar_os(id_os)
        if not ordem:
            print("Ordem de Serviço não encontrada.")
            return None
        return ordem
    except ValueError as e:
        print(f"Atenção: {e}")

