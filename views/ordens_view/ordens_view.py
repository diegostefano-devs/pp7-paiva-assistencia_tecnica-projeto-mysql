import customtkinter as ctk
from controllers.ordens_controller import abrir_ordem
from repositories.ordens_repository import buscar_tec
from controllers.cliente_controller import mostrar_um_cliente

def abrir_os_view(frame):

    for i, campo in enumerate(['ID Cliente', 'Aparelho', 'Problema']):
        ctk.CTkLabel(frame, text=f"{campo}: ", font=("Roboto", 20, 'bold')).grid(
            row=i, column=0, sticky='e', pady=15, padx=10)


    entry_modelo = ctk.CTkEntry(frame, width=350, placeholder_text=f"Informe o modelo do aparelho: ", font=("Roboto", 20))
    entry_modelo.grid(row=1, column=1, sticky='w', pady=15, padx=(0, 20))

    entry_cliente = ctk.CTkEntry(frame, width=350, placeholder_text="Digite o ID do cliente: ", font=("Roboto", 20))
    entry_cliente.grid(row=0, column=1, sticky='w', pady=15, padx=(0, 20))



    problema_textbox = ctk.CTkTextbox(frame, height=200, width=350)
    problema_textbox.grid(row = 2, column=1, sticky="w", pady=15, padx=(0, 20))

    label_cliente = ctk.CTkLabel(frame, text="", font=("Roboto", 14))
    label_cliente.place(x=135, y=48)

    label_tecnico = ctk.CTkLabel(frame, text="", font=('Roboto', 14))
    label_tecnico.place(x=135, y=48)

    def buscar_cliente(event=None):
        cliente = mostrar_um_cliente(entry_cliente.get())
        if cliente:
            label_cliente.configure(text=f"Cliente: {cliente['nome']}", text_color="#50fa7b")
        else:
            label_cliente.configure(text="Cliente não encontrado", text_color="#ff5555")

    entry_cliente.bind("<FocusOut>", buscar_cliente)


    def salvar_os():
        id_cliente = entry_cliente.get()
        aparelho = entry_modelo.get()
        problema = problema_textbox.get("1.0", "end-1c")

        if not id_cliente or not aparelho or not problema:
            label_aviso.configure(text="Preencha todos os campos!", text_color="#ff5555")
            return

        resultado = abrir_ordem(id_cliente, aparelho, problema)

        if resultado is not None:
            print("OS aberta com sucesso!", id_cliente, aparelho, problema)

            label_aviso.configure(text="OS aberta com sucesso!", text_color="#50fa7b")
            entry_cliente.delete(0, "end")
            entry_modelo.delete(0, "end")
            problema_textbox.delete("1.0", "end")
        else:
            label_aviso.configure(text="Erro ao abrir OS! Verifique o ID do Cliente", text_color="#ff5555")


    btn_salvar = ctk.CTkButton(frame, text="Abrir OS", font=("Roboto", 18, 'bold'), height=40, command=salvar_os)
    btn_salvar.grid(row=3, column=1, sticky="ew", pady=10, padx=(0, 20))


    label_aviso = ctk.CTkLabel(frame, text="", font=("Roboto", 16))
    label_aviso.grid(row=4, column=1, sticky="w", padx=(0, 20))

