import customtkinter as ctk
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
    
    
    cpf_excluir = ctk.CTkEntry(
        frame_centro, 
        font=("Roboto", 16), 
        width=300
    )
    cpf_excluir.pack(pady=5)
    cpf_excluir.focus()  # Garante o foco inicial para a primeira letra não sumir

    # avisos direto na tela
    lbl_aviso_exc_tec = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_exc_tec.pack(pady=5)

    def excluir():
        
        cpf = cpf_excluir.get().strip()

        # tamanho máximo
        if not cpf:
            lbl_aviso_exc_tec.configure(text="Digite o CPF do técnico!", text_color="#ef4444") 
            return
            
        if len(cpf) > 14:
            lbl_aviso_exc_tec.configure(text="O CPF deve ter no máximo 14 caracteres.", text_color="#ef4444")
            return

        try:
            excluir_tecnico(cpf)
            
            # Se deu tudo certo
            lbl_aviso_exc_tec.configure(text="Técnico excluído com sucesso!", text_color="#22c55e") # Verde
            
            # Limpa o campo
            cpf_excluir.delete(0, 'end')
            cpf_excluir.focus()
            
        except ValueError as erro:
            lbl_aviso_exc_tec.configure(text=str(erro), text_color="#ef4444")
            print(f"Validação: {erro}")
        except Exception as erro:
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