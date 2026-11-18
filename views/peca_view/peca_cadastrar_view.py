import customtkinter as ctk
from tkinter import messagebox
from controllers.peca_controllers import cadastrar_peca

def exibir_tela_cadastro(frame_centro):
    titulo = ctk.CTkLabel(
        frame_centro,
        text="Cadastrar Nova Peça",
        font=("Roboto", 16, "bold"),
        text_color="white"
    )
    titulo.pack(pady=(15, 10))

    label_nome = ctk.CTkLabel(frame_centro, text="Nome:", font=("Roboto", 14), text_color="white")
    label_nome.pack(pady=(5, 2))
    entry_nome = ctk.CTkEntry(frame_centro, width=300)
    entry_nome.pack(pady=(0, 5))

    label_categoria = ctk.CTkLabel(frame_centro, text="Categoria:", font=("Roboto", 14), text_color="white")
    label_categoria.pack(pady=(5, 2))
    entry_categoria = ctk.CTkEntry(frame_centro, width=300)
    entry_categoria.pack(pady=(0, 5))

    label_quantidade = ctk.CTkLabel(frame_centro, text="Quantidade:", font=("Roboto", 14), text_color="white")
    label_quantidade.pack(pady=(5, 2))
    entry_quantidade = ctk.CTkEntry(frame_centro, width=300)
    entry_quantidade.pack(pady=(0, 5))

    label_estado = ctk.CTkLabel(frame_centro, text="Estado (máx. 10 letras):", font=("Roboto", 14), text_color="white")
    label_estado.pack(pady=(5, 2))
    entry_estado = ctk.CTkEntry(frame_centro, width=300)
    entry_estado.pack(pady=(0, 5))

    label_preco = ctk.CTkLabel(frame_centro, text="Preço:", font=("Roboto", 14), text_color="white")
    label_preco.pack(pady=(5, 2))
    entry_preco = ctk.CTkEntry(frame_centro, width=300)
    entry_preco.pack(pady=(0, 15))

    def salvar():
        nome = entry_nome.get()
        categoria = entry_categoria.get()
        quantidade = entry_quantidade.get()
        estado = entry_estado.get()
        preco = entry_preco.get().replace(",", ".")

        try:
            cadastrar_peca(nome, categoria, quantidade, estado, preco)
            messagebox.showinfo("Sucesso", "Peça cadastrada com sucesso!")

            entry_nome.delete(0, "end")
            entry_categoria.delete(0, "end")
            entry_quantidade.delete(0, "end")
            entry_estado.delete(0, "end")
            entry_preco.delete(0, "end")

        except ValueError as erro:
            messagebox.showerror("Erro de Validação", str(erro))
        except Exception as erro:
            messagebox.showerror("Erro", f"Falha ao cadastrar peça: {erro}")

    botao_confirmar = ctk.CTkButton(
        frame_centro,
        text="Confirmar Cadastro",
        font=("Roboto", 14, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=180,
        command=salvar
    )
    botao_confirmar.pack(pady=10)
