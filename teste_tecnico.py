from controllers.tecnico_controllers import (

    cadastrar_tecnico,
    tecnico,
    atualizar_tecnico,
    excluir_tecnico
)

print("--- 1. TESTANDO ERRO DE CAMPO VAZIO ---")
try:
    cadastrar_tecnico("", "João Silva", "74999999999")
except ValueError as e:
    print(f"Passou no teste! Erro capturado: {e}")

print("\n--- 2. TESTANDO CADASTRO VÁLIDO ---")
try:
    cadastrar_tecnico("123.456.789-44", "Raul Paiva", "74999352668")
    print("Passou no teste! Técnico cadastrado com sucesso.")
except Exception as e:
    print(f"Falhou: {e}")

print("\n--- 3. TESTANDO LISTAGEM ---")
lista = tecnico()
print("Técnicos no banco:", lista)

print("\n--- 4. TESTANDO ATUALIZAÇÃO ---")
try:
    atualizar_tecnico("Raul Paiva Editado", "74977777775", "123.456.789-45")
    print("Passou no teste! Técnico atualizado.")
except Exception as e:
    print(f"Falhou: {e}")

'''print("\n--- 5. TESTANDO EXCLUSÃO ---")
try:
    excluir_tecnico("123.456.789-45")
    print("Passou no teste! Técnico excluído.")
except Exception as e:
    print(f"Falhou: {e}")'''
