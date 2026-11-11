from controllers.cliente_controller import cadastrar_cliente, clientes, excluir_cliente

# cadastrar_cliente("12345678912", "Diego Stefano", "09876543212")
print(clientes())

excluir_cliente("12345678912")

print(clientes())