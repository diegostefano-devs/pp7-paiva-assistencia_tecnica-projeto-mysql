from controllers.ordens_controller import abrir_ordem, listar_os_status, finalizar_ordem_de_servico, listar_todas_os
from controllers.cliente_controller import cadastrar_cliente
from controllers.itens_ordens_controller import abrir_orcamento

cadastrar_cliente("123.456.789-01", "Diego Stefano", "09876543212223")
# print(clientes())

# excluir_cliente("12345678912")

# print(clientes())

# abrir_ordem("a", "Celular", "Quebrado")

# finalizar_ordem_de_servico(4, "CONCLUIDA")

# resultado = list(listar_todas_os())
# for os in resultado:
#     print(f"ID: {os['id']}, STATUS: {os['status']}")

# resultado = list(listar_os_status("AGUARDANDO APROVA"))
# for os in resultado:
#     print(f"ID: {os['id']}, STATUS: {os['status']}")