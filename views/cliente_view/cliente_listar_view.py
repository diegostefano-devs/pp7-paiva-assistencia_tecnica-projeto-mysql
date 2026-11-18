import customtkinter as ctk
from controllers.cliente_controller import mostrar_clientes

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

    clientes = mostrar_clientes()

    if clientes:
        for cli in clientes:
            card = ctk.CTkFrame(frame_lista, fg_color="#2b2b2b", corner_radius=6)
            card.pack(fill=ctk.X, pady=5, padx=5)

            texto_info = f"ID: {cli['id']} | Nome: {cli['nome']}  |  CPF: {cli['cpf']}  |  Tel: {cli['telefone']}"
            ctk.CTkLabel(card, text=texto_info, font=("Roboto", 14), text_color="white").pack(side=ctk.LEFT, padx=15, pady=10)