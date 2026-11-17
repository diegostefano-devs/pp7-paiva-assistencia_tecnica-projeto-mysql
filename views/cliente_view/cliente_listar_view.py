import customtkinter as ctk

def exibir_tela_listar(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Lista de Clientes Cadastrados", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    frame_lista = ctk.CTkScrollableFrame(frame_centro, fg_color="#212121", width=500, height=350)
    frame_lista.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)

    clientes = [
        {"nome": "Virginia Fonseca", "cpf": "109.851.149-41", "telefone": "(11) 98146-1126"},
        {"nome": "Zé Felipe", "cpf": "537.248.059-18", "telefone": "(11) 98137-7072"}
    ]

    for cli in clientes:
        card = ctk.CTkFrame(frame_lista, fg_color="#2b2b2b", corner_radius=6)
        card.pack(fill=ctk.X, pady=5, padx=5)

        texto_info = f"Nome: {cli['nome']}  |  CPF: {cli['cpf']}  |  Tel: {cli['telefone']}"
        ctk.CTkLabel(card, text=texto_info, font=("Roboto", 14), text_color="white").pack(side=ctk.LEFT, padx=15, pady=10)