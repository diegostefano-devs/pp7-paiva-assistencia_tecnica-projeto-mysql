import customtkinter as ctk
from controllers.tecnico_controllers import atualizar_tecnico


cpf_entry_alterar = None
novo_nome_entry = None
novo_telefone_entry = None
lbl_aviso_alt_tec = None

def exibir_tela_alterar(frame_centro):
    global cpf_entry_alterar, novo_nome_entry, novo_telefone_entry, lbl_aviso_alt_tec
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Alterar Dados do Técnico", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)


    ctk.CTkLabel(frame_centro, text="CPF do Técnico a Alterar:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry_alterar = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry_alterar.pack(pady=5)
    cpf_entry_alterar.focus()  


    ctk.CTkLabel(frame_centro, text="Novo Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_nome_entry.pack(pady=5)


    ctk.CTkLabel(frame_centro, text="Novo Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_telefone_entry.pack(pady=5)
    
    lbl_aviso_alt_tec = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_alt_tec.pack(pady=5)

    def alterar():
        cpf = cpf_entry_alterar.get().strip()
        novo_nome = novo_nome_entry.get().strip()
        novo_telefone = novo_telefone_entry.get().strip()

        # limites máximos de caracteres
        if not cpf or not novo_nome or not novo_telefone:
            lbl_aviso_alt_tec.configure(text="Preencha todos os campos!", text_color="#ef4444")
            return
            
        if len(cpf) > 14:
            lbl_aviso_alt_tec.configure(text="O CPF deve ter no máximo 14 caracteres.", text_color="#ef4444")
            return
            
        if len(novo_nome) > 50:
            lbl_aviso_alt_tec.configure(text="O nome deve ter no máximo 50 caracteres.", text_color="#ef4444")
            return
            
        if len(novo_telefone) > 20:
            lbl_aviso_alt_tec.configure(text="O telefone deve ter no máximo 20 caracteres.", text_color="#ef4444")
            return

        try:
            atualizar_tecnico(novo_nome, novo_telefone, cpf)
            
            lbl_aviso_alt_tec.configure(text="Técnico alterado com sucesso!", text_color="#22c55e") 
            print(f"Alterando técnico CPF: {cpf} para Nome: {novo_nome}, Tel: {novo_telefone}")
            
            # Limpa os campos 
            cpf_entry_alterar.delete(0, 'end')
            novo_nome_entry.delete(0, 'end')
            novo_telefone_entry.delete(0, 'end')
            cpf_entry_alterar.focus()
            
        except ValueError as erro:
            lbl_aviso_alt_tec.configure(text=str(erro), text_color="#ef4444")
            print(f"Validação: {erro}")
        except Exception as erro:
            lbl_aviso_alt_tec.configure(text=f"Erro ao alterar: {erro}", text_color="#ef4444")
            print(f"Erro: {erro}")

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Alteração", 
        font=("Roboto", 18, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=alterar
    ).pack(pady=15)