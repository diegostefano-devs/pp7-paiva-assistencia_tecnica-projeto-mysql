import customtkinter as ctk
from controllers.peca_controllers import cadastrar_peca

nome_entry = None
categoria_entry = None
quantidade_entry = None
estado_entry = None
preco_entry = None
lbl_aviso = None

def exibir_tela_cadastro(frame_centro):
    global nome_entry, categoria_entry, quantidade_entry, estado_entry, preco_entry, lbl_aviso

    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Cadastrar Nova Peça", 
        font=("Roboto", 16, "bold"), 
        text_color="white"
    ).pack(pady=15)

    ctk.CTkLabel(frame_centro, text="Nome:", font=("Roboto", 16), text_color="white").pack(pady=2)
    nome_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    nome_entry.pack(pady=4)

    ctk.CTkLabel(frame_centro, text="Categoria:", font=("Roboto", 16), text_color="white").pack(pady=2)
    categoria_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    categoria_entry.pack(pady=4)

    ctk.CTkLabel(frame_centro, text="Quantidade:", font=("Roboto", 16), text_color="white").pack(pady=2)
    quantidade_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    quantidade_entry.pack(pady=4)

    ctk.CTkLabel(frame_centro, text="Estado (máx. 10 letras):", font=("Roboto", 16), text_color="white").pack(pady=2)
    estado_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    estado_entry.pack(pady=4)

    ctk.CTkLabel(frame_centro, text="Preço:", font=("Roboto", 16), text_color="white").pack(pady=2)
    preco_entry = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    preco_entry.pack(pady=4)

    lbl_aviso = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso.pack(pady=5)

    def salvar():
        nome = nome_entry.get().strip()
        categoria = categoria_entry.get().strip()
        quantidade_str = quantidade_entry.get().strip()
        estado = estado_entry.get().strip()
        preco_str = preco_entry.get().strip().replace(",", ".")

        if not nome or not categoria or not quantidade_str or not estado or not preco_str:
            lbl_aviso.configure(text="Preencha todos os campos!", text_color="#ef4444")
            return

        if len(estado) > 10:
            lbl_aviso.configure(text="O estado deve ter no máximo 10 letras!", text_color="#ef4444")
            return

        try:
            quantidade = int(quantidade_str)
            preco = float(preco_str)
        except ValueError:
            lbl_aviso.configure(text="Quantidade ou preço inválidos!", text_color="#ef4444")
            return

        try:
            peca = cadastrar_peca(nome, categoria, quantidade, estado, preco)
            lbl_aviso.configure(text="Peça cadastrada com sucesso!", text_color="#22c55e")
            print(f"Sucesso ao capturar: {nome}, {categoria}, {quantidade}, {estado}, {preco}")

            nome_entry.delete(0, 'end')
            categoria_entry.delete(0, 'end')
            quantidade_entry.delete(0, 'end')
            estado_entry.delete(0, 'end')
            preco_entry.delete(0, 'end')

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
