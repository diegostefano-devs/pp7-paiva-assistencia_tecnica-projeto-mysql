import customtkinter as ctk

# Importando as funções dos outros arquivos
from views.tecnico_view.tecnico_cadastrar_view import exibir_tela_cadastro
from views.tecnico_view.tecnico_alterar_view import exibir_tela_alterar
from views.tecnico_view.tecnico_excluir_view import exibir_tela_excluir
from views.tecnico_view.tecnico_listar_view import exibir_tela_listar

# Configuração inicial do CustomTkinter para o Modo Escuro
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Tela de técnico")
janela.geometry("800x600")

# Faixa superior
faixa = ctk.CTkFrame(janela, fg_color="#2d2853", height=90, corner_radius=0)
faixa.pack(side=ctk.TOP, fill=ctk.X)

titulo = ctk.CTkLabel(
    faixa, 
    text="Painel de controle - Técnico",
    font=("Roboto", 18, "bold"), 
    text_color="white"
)
titulo.pack(pady=25)

# Barra lateral esquerda em tom cinza escuro
frame_lateral = ctk.CTkFrame(janela, fg_color="#2b2b2b", width=200, corner_radius=0)
frame_lateral.pack(side=ctk.LEFT, fill=ctk.Y)

# Centro da tela
frame_centro = ctk.CTkFrame(janela, fg_color="#1a1a1a")
frame_centro.pack(side=ctk.RIGHT, expand=True, fill=ctk.BOTH)

# Botões da barra lateral chamando as funções dos arquivos importados
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

# Botão Listar na barra lateral
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

janela.mainloop()