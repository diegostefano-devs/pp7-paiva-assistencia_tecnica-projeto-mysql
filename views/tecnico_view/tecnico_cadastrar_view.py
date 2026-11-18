import customtkinter as ctk
from controllers.tecnico_controllers import cadastrar_tecnico

# Variáveis globais para armazenar os campos
nome_entry = None
cpf_entry = None
telefone_entry = None
lbl_aviso_cad_tec = None

def exibir_tela_cadastro(frame_centro):
    global nome_entry, cpf_entry, telefone_entry, lbl_aviso_cad_tec
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Cadastrar Novo Técnico", 
        font=("Roboto", 16, "bold"), 
        text_color="white"
    ).pack(pady=20)

    # --- CAMPO NOME ---
    ctk.CTkLabel(frame_centro, text="Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    nome_entry.pack(pady=5)
    nome_entry.focus()  # Garante o foco inicial para a primeira letra não sumir

    # --- CAMPO CPF ---
    ctk.CTkLabel(frame_centro, text="CPF:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_entry.pack(pady=5)

    # --- CAMPO TELEFONE ---
    ctk.CTkLabel(frame_centro, text="Telefone:", font=("Roboto", 16), text_color="white").pack(pady=2)
    telefone_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    telefone_entry.pack(pady=5)

    lbl_aviso_cad_tec = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_cad_tec.pack(pady=5)

    def salvar():
        nome = nome_entry.get().strip()
        cpf = cpf_entry.get().strip()
        telefone = telefone_entry.get().strip()

        # Validações de preenchimento e limites máximos de caracteres
        if not nome or not cpf or not telefone:
            lbl_aviso_cad_tec.configure(text="Preencha todos os campos!", text_color="#ef4444") 
            return
            
        if len(nome) > 50:
            lbl_aviso_cad_tec.configure(text="O nome deve ter no máximo 50 caracteres.", text_color="#ef4444")
            return
            
        if len(cpf) > 14:
            lbl_aviso_cad_tec.configure(text="O CPF deve ter no máximo 14 caracteres.", text_color="#ef4444")
            return
            
        if len(telefone) > 20:
            lbl_aviso_cad_tec.configure(text="O telefone deve ter no máximo 20 caracteres.", text_color="#ef4444")
            return

        try:
            # Chama a função do controller
            cadastrar_tecnico(cpf, nome, telefone)
            
            lbl_aviso_cad_tec.configure(text="Técnico cadastrado com sucesso!", text_color="#22c55e")
            print(f"Salvando: Nome: {nome}, CPF: {cpf}, Tel: {telefone}")
            
            # Limpa os campos e retorna o foco
            nome_entry.delete(0, 'end')
            cpf_entry.delete(0, 'end')
            telefone_entry.delete(0, 'end')
            nome_entry.focus()
            
        except ValueError as erro:
            lbl_aviso_cad_tec.configure(text=str(erro), text_color="#ef4444")
            print(f"Validação: {erro}")
        except Exception as erro:
            lbl_aviso_cad_tec.configure(text=f"Erro no sistema: {erro}", text_color="#ef4444")
            print(f"Erro: {erro}")

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Cadastro!", 
        font=("Roboto", 18, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=salvar
    ).pack(pady=15)