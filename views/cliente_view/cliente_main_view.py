import customtkinter as ctk

# Importando as funções dos arquivos atualizados dentro de cliente_view
from views.cliente_view.cliente_cadastrar_view import exibir_tela_cadastro
from views.cliente_view.cliente_alterar_view import exibir_tela_alterar
from views.cliente_view.cliente_excluir_view import exibir_tela_excluir
from views.cliente_view.cliente_listar_view import exibir_tela_listar


def exibir_tela_cliente(container, voltar):
    for widget in container.winfo_children():
        widget.destroy()

    faixa = ctk.CTkFrame(container, fg_color="#2d2853", height=90, corner_radius=0)
    faixa.pack(side=ctk.TOP, fill=ctk.X)

    titulo = ctk.CTkLabel(
        faixa,
        text="Painel de controle - Cliente",
        font=("Roboto", 18, "bold"),
        text_color="white"
    )
    titulo.pack(pady=25)

    frame_lateral = ctk.CTkFrame(container, fg_color="#2b2b2b", width=200, corner_radius=0)
    frame_lateral.pack(side=ctk.LEFT, fill=ctk.Y)

    # Centro da tela
    frame_centro = ctk.CTkFrame(container, fg_color="#1a1a1a")
    frame_centro.pack(side="right", expand=True, fill=ctk.BOTH)

    botao_cadastrar = ctk.CTkButton(
        frame_lateral,
        text="Cadastrar",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=150,
        command=lambda: exibir_tela_cadastro(frame_centro)
    )
    botao_cadastrar.pack(pady=20, padx=20)

    botao_alterar = ctk.CTkButton(
        frame_lateral,
        text="Alterar",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=150,
        command=lambda: exibir_tela_alterar(frame_centro)
    )
    botao_alterar.pack(pady=10, padx=20)

    botao_excluir = ctk.CTkButton(
        frame_lateral,
        text="Excluir",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=150,
        command=lambda: exibir_tela_excluir(frame_centro)
    )
    botao_excluir.pack(pady=20, padx=20)

    botao_listar = ctk.CTkButton(
        frame_lateral,
        text="Listar",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=150,
        command=lambda: exibir_tela_listar(frame_centro)
    )
    botao_listar.pack(pady=10, padx=20)

    botao_voltar = ctk.CTkButton(
        frame_lateral,
        text="Voltar ao Menu",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=150,
        command=voltar
    )
    botao_voltar.pack(side=ctk.BOTTOM, pady=20, padx=20)