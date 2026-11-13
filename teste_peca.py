from controllers.peca_controllers import cadastrar_peca, listar_peca, atualizar_peca, excluir_peca

print("--- INICIANDO TESTES DO MÓDULO DE PEÇAS ---\n")

# 1. Teste de Cadastro Válido
try:
    print("1. Testando cadastro de nova peça...")
    cadastrar_peca("Fundo", "Vidro", 10, "Novo", 285.00)
    print("-> Sucesso ao cadastrar peça!\n")
except ValueError as e:
    print(f"Erro de validação: {e}\n")
except Exception as e:
    print(f"Erro no sistema: {e}\n")


# 2. Teste de Cadastro com Erro (Campos obrigatórios vazios)
try:
    print("2. Testando cadastro com campos vazios (deve gerar erro)...")
    cadastrar_peca("", "Display", 5, "Novo", 100.00)
except ValueError as e:
    print(f"-> Validação funcionou corretamente: {e}\n")
except Exception as e:
    print(f"Erro no sistema: {e}\n")


# 3. Teste de Listagem
try:
    print("3. Testando listagem de peças cadastradas no banco...")
    pecas = listar_peca()
    if pecas:
        print(f"-> Total de peças encontradas: {len(pecas)}")
        for p in pecas:
            print(f"   [ID: {p['id']}] Nome: {p['nome']} | Categoria: {p['categoria']} | Qtd: {p['quantidade']} | Preço: R$ {p['preco']}")
    else:
        print("-> Nenhuma peça encontrada no banco.")
    print()
except Exception as e:
    print(f"Erro ao listar: {e}\n")


# 4. Teste de Atualização (Pegando o primeiro ID disponível se houver)
try:
    pecas = listar_peca()
    if pecas:
        primeiro_id = pecas[0]['id']
        print(f"4. Testando atualização da peça com ID {primeiro_id}...")
        atualizar_peca(primeiro_id, "Tela Atualizada", "Display", 10, "Novo", 230.00)
        print("-> Peça atualizada com sucesso!\n")
    else:
        print("4. Nenhuma peça para atualizar.\n")
except ValueError as e:
    print(f"Erro de validação: {e}\n")
except Exception as e:
    print(f"Erro no sistema: {e}\n")