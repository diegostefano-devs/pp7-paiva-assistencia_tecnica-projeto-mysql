import customtkinter as ctk

cpf_entry_alterar = None
novo_nome_entry = None
novo_telefone_entry = None

def exibir_tela_alterar(frame_centro):
    global cpf_entry_alterar, novo_nome_entry, novo_telefone_entry
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Alterar Dados do Técnico", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Técnico a Alterar:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry_alterar = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry_alterar.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_nome_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_telefone_entry.pack(pady=5)

    def alterar():
        print(f"Alterando técnico CPF: {cpf_entry_alterar.get()}")

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Alteração", 
        font=("Roboto", 18, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=alterar
    ).pack(pady=20)