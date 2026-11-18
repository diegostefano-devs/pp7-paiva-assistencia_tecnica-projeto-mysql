import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import customtkinter as ctk

from views.cliente_view.cliente_main_view import exibir_tela_cliente
from views.tecnico_view.tecnico_main_view import exibir_tela_tecnico
from views.peca_view.peca_main_view import exibir_tela_peca
from views.ordens_view.ordens_main_view import exibir_tela_ordens

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Menu Principal")
janela.geometry("800x600")

container = ctk.CTkFrame(janela, fg_color="#1a1a1a", corner_radius=0)
container.pack(expand=True, fill=ctk.BOTH)


def mostrar_menu():
    for widget in container.winfo_children():
        widget.destroy()

    faixa = ctk.CTkFrame(container, fg_color="#2d2853", height=90, corner_radius=0)
    faixa.pack(side=ctk.TOP, fill=ctk.X)

    titulo = ctk.CTkLabel(
        faixa,
        text="Menu Principal",
        font=("Roboto", 30, "bold"),
        text_color="white"
    )
    titulo.pack(pady=24)

    frame_centro = ctk.CTkFrame(container, fg_color="#1a1a1a")
    frame_centro.pack(expand=True, fill=ctk.BOTH)

    frame_botoes = ctk.CTkFrame(frame_centro, fg_color="transparent")
    frame_botoes.pack(expand=True)

    botao_cliente = ctk.CTkButton(
        frame_botoes,
        text="Cliente",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=200,
        command=lambda: exibir_tela_cliente(container, mostrar_menu)
    )
    botao_cliente.pack(pady=15)

    botao_tecnico = ctk.CTkButton(
        frame_botoes,
        text="Técnico",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=200,
        command=lambda: exibir_tela_tecnico(container, mostrar_menu)
    )
    botao_tecnico.pack(pady=15)

    botao_peca = ctk.CTkButton(
        frame_botoes,
        text="Peças",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=200,
        command=lambda: exibir_tela_peca(container, mostrar_menu)
    )
    botao_peca.pack(pady=15)

    botao_ordens = ctk.CTkButton(
        frame_botoes,
        text="Ordens de Serviço",
        font=("Roboto", 16, "bold"),
        fg_color="#2196f3",
        hover_color="#1976d2",
        text_color="white",
        width=200,
        command=lambda: exibir_tela_ordens(container, mostrar_menu)
    )
    botao_ordens.pack(pady=15)


mostrar_menu()
janela.mainloop()