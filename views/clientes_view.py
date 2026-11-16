import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

class AppClientes(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Assistência Técnica - Gestão de Clientes")
        self.geometry("800x600")
        self.resizable(False, False)
        
       
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        self.frame_menu = ctk.CTkFrame(self, width=220, fg_color="#0f172a", corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")
        
        lbl_logo = ctk.CTkLabel(self.frame_menu, text="MENU CLIENTES", font=("Roboto", 16, "bold"), text_color="#38bdf8")
        lbl_logo.pack(pady=25)
        
        
        btn_cadastrar_menu = ctk.CTkButton(
            self.frame_menu, text="Cadastrar Cliente", font=("Roboto", 13, "bold"),
            fg_color="#1d4ed8", hover_color="#2563eb", command=self.mostrar_tela_cadastrar
        )
        btn_cadastrar_menu.pack(pady=10, padx=15, fill="x")
        
        btn_alterar_menu = ctk.CTkButton(
            self.frame_menu, text="Alterar Cliente", font=("Roboto", 13, "bold"),
            fg_color="#1d4ed8", hover_color="#2563eb", command=self.mostrar_tela_alterar
        )
        btn_alterar_menu.pack(pady=10, padx=15, fill="x")
        
        btn_excluir_menu = ctk.CTkButton(
            self.frame_menu, text="Excluir Cliente", font=("Roboto", 13, "bold"),
            fg_color="#1d4ed8", hover_color="#2563eb", command=self.mostrar_tela_excluir
        )
        btn_excluir_menu.pack(pady=10, padx=15, fill="x")

        
        self.frame_conteudo = ctk.CTkFrame(self, fg_color="#121212", corner_radius=0)
        self.frame_conteudo.grid(row=0, column=1, sticky="nsew")
        
        
        self.mostrar_tela_cadastrar()

    def limpar_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    
    def mostrar_tela_cadastrar(self):
        self.limpar_conteudo()
        
        titulo = ctk.CTkLabel(self.frame_conteudo, text="CADASTRAR NOVO CLIENTE", font=("Roboto", 20, "bold"), text_color="#ffffff")
        titulo.pack(pady=25)
        
        campos = ["Nome Completo", "CPF", "Telefone", "E-mail", "Endereço"]
        self.entries_cad = {}
        
        for campo in campos:
            frame_linha = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
            frame_linha.pack(pady=8, padx=30, fill="x")
            
            lbl = ctk.CTkLabel(frame_linha, text=f"{campo}:", font=("Roboto", 13, "bold"), width=130, anchor="w")
            lbl.pack(side="left")
            
            entry = ctk.CTkEntry(frame_linha, width=380, placeholder_text=f"Digite o {campo.lower()}", fg_color="#1a1a1a", border_color="#1d4ed8")
            entry.pack(side="right", expand=True)
            self.entries_cad[campo] = entry
            
        btn_salvar = ctk.CTkButton(
            self.frame_conteudo, text="Salvar Cadastro", font=("Roboto", 13, "bold"),
            fg_color="#1d4ed8", hover_color="#2563eb", width=180, command=self.acao_salvar_cadastro
        )
        btn_salvar.pack(pady=30)

    
    def mostrar_tela_alterar(self):
        self.limpar_conteudo()
        
        titulo = ctk.CTkLabel(self.frame_conteudo, text="ALTERAR DADOS DO CLIENTE", font=("Roboto", 20, "bold"), text_color="#ffffff")
        titulo.pack(pady=25)
        
        campos = ["ID do Cliente", "Novo Nome", "Novo CPF", "Novo Telefone", "Novo E-mail", "Novo Endereço"]
        self.entries_alt = {}
        
        for campo in campos:
            frame_linha = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
            frame_linha.pack(pady=6, padx=30, fill="x")
            
            lbl = ctk.CTkLabel(frame_linha, text=f"{campo}:", font=("Roboto", 13, "bold"), width=130, anchor="w")
            lbl.pack(side="left")
            
            entry = ctk.CTkEntry(frame_linha, width=380, placeholder_text=f"Digite {campo.lower()}", fg_color="#1a1a1a", border_color="#1d4ed8")
            entry.pack(side="right", expand=True)
            self.entries_alt[campo] = entry
            
        btn_atualizar = ctk.CTkButton(
            self.frame_conteudo, text="Salvar Alterações", font=("Roboto", 13, "bold"),
            fg_color="#2563eb", hover_color="#1d4ed8", width=180, command=self.acao_salvar_alteracao
        )
        btn_atualizar.pack(pady=25)

    
    def mostrar_tela_excluir(self):
        self.limpar_conteudo()
        
        titulo = ctk.CTkLabel(self.frame_conteudo, text="EXCLUIR CLIENTE", font=("Roboto", 20, "bold"), text_color="#ffffff")
        titulo.pack(pady=35)
        
        frame_linha = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        frame_linha.pack(pady=15, padx=30, fill="x")
        
        lbl = ctk.CTkLabel(frame_linha, text="ID do Cliente:", font=("Roboto", 14, "bold"), width=130, anchor="w")
        lbl.pack(side="left")
        
        self.entry_exc_id = ctk.CTkEntry(frame_linha, width=380, placeholder_text="Digite o ID do cliente que deseja excluir", fg_color="#1a1a1a", border_color="#1d4ed8")
        self.entry_exc_id.pack(side="right", expand=True)
        
        aviso = ctk.CTkLabel(self.frame_conteudo, text="Aviso: A exclusão é permanente após a confirmação.", font=("Roboto", 12), text_color="#94a3b8")
        aviso.pack(pady=10)

        btn_excluir = ctk.CTkButton(
            self.frame_conteudo, text="Excluir Cliente", font=("Roboto", 13, "bold"),
            fg_color="#0f172a", hover_color="#1e293b", border_color="#1d4ed8", border_width=1, width=180, command=self.acao_confirmar_exclusao
        )
        btn_excluir.pack(pady=30)

    
    def acao_salvar_cadastro(self):
        nome = self.entries_cad["Nome Completo"].get()
        if not nome:
            messagebox.showwarning("Aviso", "Preencha o nome do cliente!")
            return
        
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        for e in self.entries_cad.values(): e.delete(0, 'end')

    def acao_salvar_alteracao(self):
        id_c = self.entries_alt["ID do Cliente"].get()
        if not id_c:
            messagebox.showwarning("Aviso", "Informe o ID do cliente a ser alterado!")
            return
        
        messagebox.showinfo("Sucesso", f"Cliente ID {id_c} alterado com sucesso!")
        for e in self.entries_alt.values(): e.delete(0, 'end')

    def acao_confirmar_exclusao(self):
        id_c = self.entry_exc_id.get()
        if not id_c:
            messagebox.showwarning("Aviso", "Informe o ID do cliente!")
            return
        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o cliente ID {id_c}?"):
           
            messagebox.showinfo("Sucesso", f"Cliente ID {id_c} excluído com sucesso!")
            self.entry_exc_id.delete(0, 'end')

if __name__ == "__main__":
    app = AppClientes()
    app.mainloop()