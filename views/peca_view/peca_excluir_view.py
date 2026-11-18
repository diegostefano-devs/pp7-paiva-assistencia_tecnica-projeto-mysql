import customtkinter as ctk
from controllers.peca_controllers import deletar_peca

def exibir_tela_excluir(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro,
        text="Excluir Peça",
        font=("Roboto", 18, "bold"),
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="ID da Peça a Excluir:", font=("Roboto", 16), text_color="white").pack(pady=2)
    id_excluir = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    id_excluir.pack(pady=5)

    lbl_aviso_exc = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_exc.pack(pady=5)

    def excluir():
        peca_id = id_excluir.get().strip()

        if not peca_id:
            lbl_aviso_exc.configure(text="Digite o ID da peça!", text_color="#ef4444")
            return

        try:
            deletar_peca(peca_id)
            lbl_aviso_exc.configure(text="Peça excluída com sucesso!", text_color="#22c55e")
            id_excluir.delete(0, "end")

        except ValueError as erro:
            lbl_aviso_exc.configure(text=str(erro), text_color="#ef4444")
        except Exception as erro:
            lbl_aviso_exc.configure(text=f"Erro ao excluir: {erro}", text_color="#ef4444")

    ctk.CTkButton(
        frame_centro,
        text="Confirmar Exclusão",
        font=("Roboto", 16, "bold"),
        fg_color="#ef4444",
        hover_color="#dc2626",
        text_color="white",
        width=200,
        command=excluir
    ).pack(pady=15)
