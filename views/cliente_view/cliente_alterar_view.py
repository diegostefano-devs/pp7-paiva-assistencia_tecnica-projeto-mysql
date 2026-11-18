import customtkinter as ctk
from controllers.cliente_controller import atualizar_cliente    

cpf_entry_alterar = None
novo_nome_entry = None
novo_telefone_entry = None
lbl_aviso_alt = None

def exibir_tela_alterar(frame_centro):
    global cpf_entry_alterar, novo_nome_entry, novo_telefone_entry, lbl_aviso_alt
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Alterar Dados do Cliente", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Cliente a Alterar:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry_alterar = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry_alterar.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_nome_entry.pack(pady=5)

    ctk.CTkLabel(frame_centro, text="Novo Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    novo_telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    novo_telefone_entry.pack(pady=5)

    lbl_aviso_alt = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_alt.pack(pady=5)

    def alterar():
        cpf = cpf_entry_alterar.get()
        novo_nome = novo_nome_entry.get()
        novo_telefone = novo_telefone_entry.get()

        if not cpf or not novo_nome.strip() or not novo_telefone.strip():
            lbl_aviso_alt.configure(text="Preencha todos os campos!", text_color="#ef4444")
            return

        try:  
            atualizar_cliente(novo_nome, novo_telefone, cpf)
            lbl_aviso_alt.configure(text="Cliente alterado com sucesso!", text_color="#22c55e") 
            print(f"Alterando cliente CPF: {cpf} para Nome: {novo_nome}, Tel: {novo_telefone}")
                
                
            cpf_entry_alterar.delete(0, 'end')
            novo_nome_entry.delete(0, 'end')
            novo_telefone_entry.delete(0, 'end')
        except ValueError as erro:
            lbl_aviso_alt.configure(text=f"{erro}", text_color="#ef4444")
        except Exception as erro:
            lbl_aviso_alt.configure(text=f"Erro ao alterar: {erro}", text_color="#ef4444")
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