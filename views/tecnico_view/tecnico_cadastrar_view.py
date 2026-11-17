import customtkinter as ctk

# Variáveis globais para armazenar os campos (opcional, dependendo de como vai salvar)
nome_entry = None
cpf_entry = None
telefone_entry = None

def exibir_tela_cadastro(frame_centro):
    global nome_entry, cpf_entry, telefone_entry
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Cadastrar Novo Técnico", 
        font=("Roboto", 16, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    nome_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="CPF:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    telefone_entry.pack(pady=5)

    def salvar():
        # Lógica para salvar os dados aqui
        print(f"Salvando: {nome_entry.get()}, {cpf_entry.get()}, {telefone_entry.get()}")

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Cadastro", 
        font=("Roboto", 18, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=salvar
    ).pack(pady=20)