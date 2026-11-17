import customtkinter as ctk

def exibir_tela_listar(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Lista de Técnicos Cadastrados", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    frame_lista = ctk.CTkScrollableFrame(frame_centro, fg_color="#212121", width=500, height=350)
    frame_lista.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)

    tecnicos = [
        {"nome": "Luiz Inácio", "cpf": "123.456.789-00", "telefone": "(74) 99999-1111"},
        {"nome": "Flávio Bolsonaro", "cpf": "987.654.321-11", "telefone": "(74) 98888-2222"}
    ]

    for tec in tecnicos:
        card = ctk.CTkFrame(frame_lista, fg_color="#2b2b2b", corner_radius=6)
        card.pack(fill=ctk.X, pady=5, padx=5)

        texto_info = f"Nome: {tec['nome']}  |  CPF: {tec['cpf']}  |  Tel: {tec['telefone']}"
        ctk.CTkLabel(card, text=texto_info, font=("Roboto", 14), text_color="white").pack(side=ctk.LEFT, padx=15, pady=10)