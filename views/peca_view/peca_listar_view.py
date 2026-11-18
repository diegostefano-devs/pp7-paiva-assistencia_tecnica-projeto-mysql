import customtkinter as ctk
from repositories.peca_repository import listar_peca

def exibir_tela_listar(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro,
        text="Lista de Peças Cadastradas",
        font=("Roboto", 18, "bold"),
        text_color="white"
    ).pack(pady=20)

    frame_lista = ctk.CTkScrollableFrame(frame_centro, fg_color="#212121", width=500, height=350)
    frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

    try:
        pecas = listar_peca()

        if not pecas:
            ctk.CTkLabel(
                frame_lista,
                text="Nenhuma peça cadastrada no banco de dados.",
                font=("Roboto", 14),
                text_color="white"
            ).pack(pady=20)
            return

        for peca in pecas:
            card = ctk.CTkFrame(frame_lista, fg_color="#2b2b2b", corner_radius=6)
            card.pack(fill="x", pady=5, padx=5)

            texto_info = (
                f"ID: {peca['id']}  |  Nome: {peca['nome']}  |  Cat.: {peca['categoria']}\n"
                f"Qtd: {peca['quantidade']}  |  Estado: {peca['estado']}  |  Preço: R$ {peca['preco']:.2f}"
            )
            ctk.CTkLabel(
                card,
                text=texto_info,
                font=("Roboto", 13),
                text_color="white",
                justify="left"
            ).pack(side="left", padx=15, pady=10)

    except Exception as erro:
        ctk.CTkLabel(
            frame_lista,
            text=f"Erro ao carregar peças: {erro}",
            font=("Roboto", 14, "bold"),
            text_color="#ef4444"
        ).pack(pady=20)
