import customtkinter as ctk

# 1. IMPORTAÇÃO DA FUNÇÃO DO SEU CONTROLLER
from controllers.tecnico_controllers import excluir_tecnico

cpf_excluir = None
lbl_aviso_exc_tec = None

def exibir_tela_excluir(frame_centro):
    global cpf_excluir, lbl_aviso_exc_tec
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Excluir Técnico", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Técnico a Excluir:", font=("Roboto", 16), text_color="white").pack(pady=2)
    
    # Campo de CPF livre de bugs de validação de tecla
    cpf_excluir = ctk.CTkEntry(
        frame_centro, 
        font=("Roboto", 16), 
        width=300
    )
    cpf_excluir.pack(pady=5)
    cpf_excluir.focus()  # Garante o foco inicial para a primeira letra não sumir

    # Label para os avisos direto na tela
    lbl_aviso_exc_tec = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_exc_tec.pack(pady=5)

    def excluir():
        # 1. Pega o valor do CPF com .get()
        cpf = cpf_excluir.get().strip()

        # 2. Validações básicas e de tamanho máximo
        if not cpf:
            lbl_aviso_exc_tec.configure(text="Digite o CPF do técnico!", text_color="#ef4444") # Vermelho
            return
            
        if len(cpf) > 14:
            lbl_aviso_exc_tec.configure(text="O CPF deve ter no máximo 14 caracteres.", text_color="#ef4444")
            return

        try:
            # 3. CHAMADA REAL DA SUA FUNÇÃO DO CONTROLLER QUE EXECUTA O DELETE NO MYSQL
            excluir_tecnico(cpf)
            
            # Se deu tudo certo no banco:
            lbl_aviso_exc_tec.configure(text="Técnico excluído com sucesso!", text_color="#22c55e") # Verde
            
            # Limpa o campo e foca novamente
            cpf_excluir.delete(0, 'end')
            cpf_excluir.focus()
            
        except ValueError as erro:
            # Captura os erros de validação vindos do controller (ex: CPF não encontrado)
            lbl_aviso_exc_tec.configure(text=str(erro), text_color="#ef4444")
            print(f"Validação: {erro}")
        except Exception as erro:
            # Se der algum erro de conexão ou de SQL, exibe na tela o motivo exato
            lbl_aviso_exc_tec.configure(text=f"Erro ao excluir no banco: {erro}", text_color="#ef4444")
            print(f"Erro detalhado: {erro}")

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