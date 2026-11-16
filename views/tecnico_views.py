import customtkinter as ctk



ctk.set_appearance_mode('dark')


janela = ctk.CTk()
janela.title("Sistema de Assistência Técnica - Gestão de Técnico")
janela.geometry("800x600")
janela.resizable(False, False)


janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=1)


entries_cad = {}
entries_alt = {}
entry_exc_id = None

def limpar_conteudo():
    
    for widget in frame_conteudo.winfo_children():
        widget.destroy()


def mostrar_tela_cadastrar():
    limpar_conteudo()
    global entries_cad
    
    titulo = ctk.CTkLabel(frame_conteudo, text="CADASTRAR NOVO TÉCNICO", font=("Roboto", 20, "bold"), text_color="#ffffff")
    titulo.pack(pady=25)
    
    campos = ["Nome Completo", "CPF", "Telefone", "E-mail", "Endereço"]
    entries_cad = {}
    
    for campo in campos:
        frame_linha = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
        frame_linha.pack(pady=8, padx=30, fill="x")
        
        lbl = ctk.CTkLabel(frame_linha, text=f"{campo}:", font=("Roboto", 13, "bold"), width=130, anchor="w")
        lbl.pack(side="left")
        
        entry = ctk.CTkEntry(frame_linha, width=380, placeholder_text=f"Digite o {campo.lower()}", fg_color="#1a1a1a", border_color="#1d4ed8")
        entry.pack(side="right", expand=True)
        entries_cad[campo] = entry
        
    btn_salvar = ctk.CTkButton(
        frame_conteudo, text="Salvar Cadastro", font=("Roboto", 13, "bold"),
        fg_color="#1d4ed8", hover_color="#2563eb", width=180, command=acao_salvar_cadastro
    )
    btn_salvar.pack(pady=30)


def mostrar_tela_alterar():
    limpar_conteudo()
    global entries_alt
    
    titulo = ctk.CTkLabel(frame_conteudo, text="ALTERAR DADOS DO TÉCNICO", font=("Roboto", 20, "bold"), text_color="#ffffff")
    titulo.pack(pady=25)
    
    campos = ["ID do Técnico", "Novo Nome", "Novo CPF", "Novo Telefone", "Novo E-mail", "Novo Endereço"]
    entries_alt = {}
    
    for campo in campos:
        frame_linha = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
        frame_linha.pack(pady=6, padx=30, fill="x")
        
        lbl = ctk.CTkLabel(frame_linha, text=f"{campo}:", font=("Roboto", 13, "bold"), width=130, anchor="w")
        lbl.pack(side="left")
        
        entry = ctk.CTkEntry(frame_linha, width=380, placeholder_text=f"Digite {campo.lower()}", fg_color="#1a1a1a", border_color="#1d4ed8")
        entry.pack(side="right", expand=True)
        entries_alt[campo] = entry
        
    btn_atualizar = ctk.CTkButton(
        frame_conteudo, text="Salvar Alterações", font=("Roboto", 13, "bold"),
        fg_color="#2563eb", hover_color="#1d4ed8", width=180, command=acao_salvar_alteracao
    )
    btn_atualizar.pack(pady=25)


def mostrar_tela_excluir():
    limpar_conteudo()
    global entry_exc_id
    
    titulo = ctk.CTkLabel(frame_conteudo, text="EXCLUIR TÉCNICO", font=("Roboto", 20, "bold"), text_color="#ffffff")
    titulo.pack(pady=35)
    
    frame_linha = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_linha.pack(pady=15, padx=30, fill="x")
    
    lbl = ctk.CTkLabel(frame_linha, text="ID do Técnico:", font=("Roboto", 14, "bold"), width=130, anchor="w")
    lbl.pack(side="left")
    
    entry_exc_id = ctk.CTkEntry(frame_linha, width=380, placeholder_text="Digite o ID do Técnico que deseja excluir", fg_color="#1a1a1a", border_color="#1d4ed8")
    entry_exc_id.pack(side="right", expand=True)
    
    aviso = ctk.CTkLabel(frame_conteudo, text="Aviso: A exclusão é permanente após a confirmação.", font=("Roboto", 12), text_color="#94a3b8")
    aviso.pack(pady=10)

    btn_excluir = ctk.CTkButton(
        frame_conteudo, text="Excluir Técnico", font=("Roboto", 13, "bold"),
        fg_color="#0f172a", hover_color="#1e293b", border_color="#1d4ed8", border_width=1, width=180, command=acao_confirmar_exclusao
    )
    btn_excluir.pack(pady=30)


def acao_salvar_cadastro():
    nome = entries_cad["Nome Completo"].get()
    if not nome:
        messagebox.showwarning("Aviso", "Preencha o nome do Técnico!")
        return
    
    messagebox.showinfo("Sucesso", f"Técnico {nome} cadastrado com sucesso!")
    for e in entries_cad.values():
        e.delete(0, 'end')

def acao_salvar_alteracao():
    id_c = entries_alt["ID do Técnico"].get()
    if not id_c:
        messagebox.showwarning("Aviso", "Informe o ID do Técnico a ser alterado!")
        return
        
    messagebox.showinfo("Sucesso", f"Técnico ID {id_c} alterado com sucesso!")
    for e in entries_alt.values():
        e.delete(0, 'end')

def acao_confirmar_exclusao():
    id_c = entry_exc_id.get()
    if not id_c:
        messagebox.showwarning("Aviso", "Informe o ID do Técnico!")
        return
        
    if messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o Técnico ID {id_c}?"):
        messagebox.showinfo("Sucesso", f"Técnico ID {id_c} excluído com sucesso!")
        entry_exc_id.delete(0, 'end')



frame_menu = ctk.CTkFrame(janela, width=220, fg_color="#0f172a", corner_radius=0)
frame_menu.grid(row=0, column=0, sticky="nsew")

lbl_logo = ctk.CTkLabel(frame_menu, text="MENU TÉCNICOS", font=("Roboto", 16, "bold"), text_color="#38bdf8")
lbl_logo.pack(pady=25)


btn_cadastrar_menu = ctk.CTkButton(
    frame_menu, text="Cadastrar Técnico", font=("Roboto", 13, "bold"),
    fg_color="#1d4ed8", hover_color="#2563eb", command=mostrar_tela_cadastrar
)
btn_cadastrar_menu.pack(pady=10, padx=15, fill="x")

btn_alterar_menu = ctk.CTkButton(
    frame_menu, text="Alterar Técnico", font=("Roboto", 13, "bold"),
    fg_color="#1d4ed8", hover_color="#2563eb", command=mostrar_tela_alterar
)
btn_alterar_menu.pack(pady=10, padx=15, fill="x")

btn_excluir_menu = ctk.CTkButton(
    frame_menu, text="Excluir Técnico", font=("Roboto", 13, "bold"),
    fg_color="#1d4ed8", hover_color="#2563eb", command=mostrar_tela_excluir
)
btn_excluir_menu.pack(pady=10, padx=15, fill="x")



frame_conteudo = ctk.CTkFrame(janela, fg_color="#121212", corner_radius=0)
frame_conteudo.grid(row=0, column=1, sticky="nsew")


mostrar_tela_cadastrar()

janela.mainloop()