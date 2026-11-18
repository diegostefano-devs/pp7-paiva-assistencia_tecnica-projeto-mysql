import customtkinter as ctk
from controllers.peca_controllers import atualizar_peca

def exibir_tela_alterar(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro,
        text="Alterar Dados da Peça",
        font=("Roboto", 18, "bold"),
        text_color="white"
    ).pack(pady=(12, 8))

    ctk.CTkLabel(frame_centro, text="ID da Peça a Alterar:", font=("Roboto", 14), text_color="white").pack(pady=1)
    id_entry_alterar = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    id_entry_alterar.pack(pady=3)

    ctk.CTkLabel(frame_centro, text="Novo Nome:", font=("Roboto", 14), text_color="white").pack(pady=1)
    novo_nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    novo_nome_entry.pack(pady=3)

    ctk.CTkLabel(frame_centro, text="Nova Categoria:", font=("Roboto", 14), text_color="white").pack(pady=1)
    nova_categoria_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    nova_categoria_entry.pack(pady=3)

    ctk.CTkLabel(frame_centro, text="Nova Quantidade:", font=("Roboto", 14), text_color="white").pack(pady=1)
    nova_quantidade_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    nova_quantidade_entry.pack(pady=3)

    ctk.CTkLabel(frame_centro, text="Novo Estado (máx. 10 letras):", font=("Roboto", 14), text_color="white").pack(pady=1)
    novo_estado_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    novo_estado_entry.pack(pady=3)

    ctk.CTkLabel(frame_centro, text="Novo Preço:", font=("Roboto", 14), text_color="white").pack(pady=1)
    novo_preco_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 14), width=300)
    novo_preco_entry.pack(pady=3)

    lbl_aviso_alt = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_alt.pack(pady=4)

    def alterar():
        peca_id = id_entry_alterar.get().strip()
        novo_nome = novo_nome_entry.get()
        nova_categoria = nova_categoria_entry.get()
        nova_quantidade = nova_quantidade_entry.get()
        novo_estado = novo_estado_entry.get()
        novo_preco = novo_preco_entry.get().replace(",", ".")

        if not peca_id or not novo_nome or not nova_categoria or not nova_quantidade or not novo_estado or not novo_preco:
            lbl_aviso_alt.configure(text="Preencha todos os campos!", text_color="#ef4444")
            return

        try:
            atualizar_peca(peca_id, novo_nome, nova_categoria, nova_quantidade, novo_estado, novo_preco)
            lbl_aviso_alt.configure(text="Peça alterada com sucesso!", text_color="#22c55e")

            id_entry_alterar.delete(0, "end")
            novo_nome_entry.delete(0, "end")
            nova_categoria_entry.delete(0, "end")
            nova_quantidade_entry.delete(0, "end")
            novo_estado_entry.delete(0, "end")
            novo_preco_entry.delete(0, "end")

        except ValueError as erro:
            lbl_aviso_alt.configure(text=str(erro), text_color="#ef4444")
        except Exception as erro:
            lbl_aviso_alt.configure(text=f"Erro ao alterar: {erro}", text_color="#ef4444")

    ctk.CTkButton(
        frame_centro,
        text="Confirmar Alteração",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=200,
        command=alterar
    ).pack(pady=8)
