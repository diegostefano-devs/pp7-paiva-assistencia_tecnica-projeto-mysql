import customtkinter as ctk
from controllers.cliente_controller import cadastrar_cliente

nome_entry = None
cpf_entry = None
telefone_entry = None
lbl_aviso = None

def exibir_tela_cadastro(frame_centro):
    global nome_entry, cpf_entry, telefone_entry, lbl_aviso
    
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    
    ctk.CTkLabel(
        frame_centro, 
        text="Cadastrar Novo Cliente", 
        font=("Roboto", 16, "bold"), 
        text_color="white"
    ).pack(pady=20)

    
    ctk.CTkLabel(frame_centro, text="Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    nome_entry.pack(pady=5)

    
    ctk.CTkLabel(frame_centro, text="CPF:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry.pack(pady=5)

    
    ctk.CTkLabel(frame_centro, text="Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    telefone_entry.pack(pady=5)

    
    lbl_aviso = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso.pack(pady=5)

    
    def salvar():
       
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        telefone = telefone_entry.get()

        
        if not nome or not cpf or not telefone:
            lbl_aviso.configure(text="Preencha todos os campos!", text_color="#ef4444") 
            return

        try:
            cliente = cadastrar_cliente(cpf, nome, telefone)
            lbl_aviso.configure(text="Cliente cadastrado com sucesso!", text_color="#22c55e") 
            print(f"Sucesso ao capturar: {nome}, {cpf}, {telefone}")
            
        
            nome_entry.delete(0, 'end')
            cpf_entry.delete(0, 'end')
            telefone_entry.delete(0, 'end')
            
        except Exception as erro:
            lbl_aviso.configure(text=f"Erro ao salvar: {erro}", text_color="#ef4444")
            print(f"Erro: {erro}")

    
    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Cadastro", 
        font=("Roboto", 18, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=salvar
    ).pack(pady=15)