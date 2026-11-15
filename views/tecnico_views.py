import customtkinter as ctk

# Configuração inicial do CustomTkinter para o Modo Escuro
ctk.set_appearance_mode("Dark")  # Força o tema escuro ("Dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Tela de técnico")
janela.geometry("800x600")

# Faixa superior (mantivemos vermelha, mas você pode escurecer se preferir)
faixa = ctk.CTkFrame(janela, fg_color="#d32f2f", height=90, corner_radius=0)
faixa.pack(side=ctk.TOP, fill=ctk.X)

titulo = ctk.CTkLabel(
    faixa, 
    text="Painel de controle - Técnico",
    font=("Arial", 16, "bold"), 
    text_color="white"
)
titulo.pack(pady=25)

# Barra lateral esquerda em tom cinza escuro
frame_lateral = ctk.CTkFrame(janela, fg_color="#2b2b2b", width=200, corner_radius=0)
frame_lateral.pack(side=ctk.LEFT, fill=ctk.Y)

# Centro da tela com fundo escuro padrão do CustomTkinter (#212121 ou similar)
frame_centro = ctk.CTkFrame(janela, fg_color="#1a1a1a")
frame_centro.pack(side=ctk.RIGHT, expand=True, fill=ctk.BOTH)


def cadastro():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Cadastrar Novo Técnico", 
        font=("Arial", 14, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="Nome:", font=("Arial", 11), text_color="white").pack(pady=2)
    global nome_entry
    nome_entry = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    nome_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="CPF:", font=("Arial", 11), text_color="white").pack(pady=2)
    global cpf_entry
    cpf_entry = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    cpf_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Telefone:", font=("Arial", 11), text_color="white").pack(pady=2)
    global telefone_entry
    telefone_entry = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    telefone_entry.pack(pady=5)

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Cadastro", 
        font=("Arial", 11, "bold"), 
        fg_color="#4caf50", 
        hover_color="#388e3c",
        text_color="white", 
        width=200
    ).pack(pady=20)


def alterar():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Alterar Dados do Técnico", 
        font=("Arial", 14, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Técnico a Alterar:", font=("Arial", 11), text_color="white").pack(pady=2)
    global cpf_entry_alterar
    cpf_entry_alterar = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    cpf_entry_alterar.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Nome:", font=("Arial", 11), text_color="white").pack(pady=2)
    global novo_nome_entry
    novo_nome_entry = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    novo_nome_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Telefone:", font=("Arial", 11), text_color="white").pack(pady=2)
    global novo_telefone_entry
    novo_telefone_entry = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    novo_telefone_entry.pack(pady=5)

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Alteração", 
        font=("Arial", 11, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200
    ).pack(pady=20)


def excluir():
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Excluir Técnico", 
        font=("Arial", 14, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Técnico a Excluir:", font=("Arial", 11), text_color="white").pack(pady=2)
    global cpf_excluir
    cpf_excluir = ctk.CTkEntry(frame_centro, font=("Arial", 11), width=300)
    cpf_excluir.pack(pady=5)

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Exclusão", 
        font=("Arial", 11, "bold"), 
        fg_color="#f44336", 
        hover_color="#d32f2f",
        text_color="white", 
        width=200
    ).pack(pady=20)


# Botões da barra lateral
botao_cadastrar = ctk.CTkButton(
    frame_lateral,
    text="Cadastrar",
    font=("Arial", 11, "bold"),
    fg_color="#4caf50",
    hover_color="#388e3c",
    text_color="white",
    width=150,
    command=cadastro
)
botao_cadastrar.pack(pady=20, padx=20)

botao_alterar = ctk.CTkButton(
    frame_lateral,
    text="Alterar",
    font=("Arial", 11, "bold"),
    fg_color="#2196f3",
    hover_color="#1976d2",
    text_color="white",
    width=150,
    command=alterar
)
botao_alterar.pack(pady=10, padx=20)

botao_excluir = ctk.CTkButton(
    frame_lateral,
    text="Excluir",
    font=("Arial", 11, "bold"),
    fg_color="#f44336",
    hover_color="#d32f2f",
    text_color="white",
    width=150,
    command=excluir 
)
botao_excluir.pack(pady=20, padx=20)

janela.mainloop()