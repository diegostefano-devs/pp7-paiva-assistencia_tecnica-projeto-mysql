import tkinter as tk


janela = tk.Tk()
janela.title("Tela de técnico")
janela.geometry("800x600")

# faixa vermelha encima
faixa = tk.Frame(janela, bg="red", height=90)
faixa.pack(side=tk.TOP, fill=tk.X)

titulo = tk.Label(faixa, text="Painel de controle - Técnico",
                  font=("Arial", 16, "bold"), bg="red", fg="white")
titulo.pack(pady=25)

# barra cinza na esquerda
frame_lateral = tk.Frame(janela, bg="#e0e0e0", width=200)
frame_lateral.pack(side=tk.LEFT, fill=tk.Y)

# lugar onde vai aparer as coisas(nome, cpf, telefone)
frame_centro = tk.Frame(janela, bg="white")
frame_centro.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)


def cadastro():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    tk.Label(frame_centro, text="Cadastrar Novo Técnico", font=("Arial", 14, "bold"), bg="white").pack(pady=20)

    tk.Label(frame_centro, text="Nome:", font=("Arial", 11), bg="white").pack(pady=2)
    global nome_entry
    nome_entry = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    nome_entry.pack(pady=5)

    tk.Label(frame_centro, text="CPF:", font=("Arial", 11), bg="white").pack(pady=2)
    global cpf_entry
    cpf_entry = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    cpf_entry.pack(pady=5)

    tk.Label(frame_centro, text="Telefone:", font=("Arial", 11), bg="white").pack(pady=2)
    global telefone_entry
    telefone_entry = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    telefone_entry.pack(pady=5)

    tk.Button(frame_centro, text="Confirmar Cadastro", font=("Arial", 11, "bold"), bg="#4caf50", fg="white", width=20).pack(pady=20)

def alterar():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    tk.Label(frame_centro, text="Alterar Dados do Técnico", font=("Arial", 14, "bold"), bg="white").pack(pady=20)

    tk.Label(frame_centro, text="CPF do Técnico a Alterar:", font=("Arial", 11), bg="white").pack(pady=2)
    global cpf_entry_alterar
    cpf_entry_alterar = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    cpf_entry_alterar.pack(pady=5)

    tk.Label(frame_centro, text="Novo Nome:", font=("Arial", 11), bg="white").pack(pady=2)
    global novo_nome_entry
    novo_nome_entry = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    novo_nome_entry.pack(pady=5)

    tk.Label(frame_centro, text="Novo Telefone:", font=("Arial", 11), bg="white").pack(pady=2)
    global novo_telefone_entry
    novo_telefone_entry = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    novo_telefone_entry.pack(pady=5)

    tk.Button(frame_centro, text="Confirmar Alteração", font=("Arial", 11, "bold"), bg="#2196f3", fg="white", width=20).pack(pady=20)

def excluir():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    tk.Label(frame_centro, text="Excluir Técnico", font=("Arial", 14, "bold"), bg="white").pack(pady=20)

    tk.Label(frame_centro, text="CPF do Técnico a Excluir:", font=("Arial", 11), bg="white").pack(pady=2)
    global cpf_excluir
    cpf_excluir = tk.Entry(frame_centro, font=("Arial", 11), width=30)
    cpf_excluir.pack(pady=5)

    tk.Button(frame_centro, text="Confirmar Exclusão", font=("Arial", 11, "bold"), bg="#f44336", fg="white", width=20).pack(pady=20)


botao_cadastrar = tk.Button(
    frame_lateral,
    text="Cadastrar",
    font=("Arial", 11, "bold"),
    bg="#4caf50",
    fg="white",
    width=15,
    command=cadastro
)
botao_cadastrar.pack(pady=20, padx=20)

botao_alterar = tk.Button(
    frame_lateral,
    text="Alterar",
    font=("Arial", 11, "bold"),
    bg="#2196f3",
    fg="white",
    width=15,
    command=alterar
)
botao_alterar.pack(pady=10, padx=20)

botao_excluir = tk.Button(
    frame_lateral,
    text="Excluir",
    font=("Arial", 11, "bold"),
    bg="#f44336",
    fg="white",
    width=15,
    command=excluir 
)
botao_excluir.pack(pady=20, padx=20)

janela.mainloop()