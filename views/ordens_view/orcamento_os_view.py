import customtkinter as ctk
from controllers.itens_ordens_controller import abrir_orcamento
from controllers.peca_controllers import mostrar_uma_peca
from controllers.ordens_controller import mostrar_uma_os
from controllers.tecnico_controllers import mostrar_um_tecnico

ctk.set_appearance_mode('dark')
frame = ctk.CTk()
frame.title('Orçamento')
frame.geometry('800x600')



def orcamento_view(frame):
    label_titulo = ctk.CTkLabel(frame, text='ORÇAMENTO', font=('Roboto', 30, 'bold')).grid(row=0, column=2,padx=(100, 0), pady=(10, 35))

    for i, campo in enumerate(["ID da OS", "ID da Peça", "Quantidade", "Mão de Obra"]):
        ctk.CTkLabel(frame, text=f'{campo}:', font=("Robuto", 20, 'bold')).grid(
                row=i, column=0, sticky='e', pady=15, padx=(10, 10))

    entry_id_os = ctk.CTkEntry(frame, width=350, placeholder_text='Digite o ID da OS', font=('Roboto', 14))
    entry_id_os.grid(row=0, column=1, sticky='w', pady=15, padx=(0, 20))


    entry_id_peca = ctk.CTkEntry(frame, width=350, placeholder_text='Digite o ID da Peça', font=('Roboto', 14))
    entry_id_peca.grid(row=1, column=1, sticky='w', pady=15, padx=(0, 20))


    entry_quantidade = ctk.CTkEntry(frame, width=350, placeholder_text="Ex: 1", font=('Roboto', 14))
    entry_quantidade.grid(row=2, column=1, sticky='w', pady=15, padx=(0, 20))


    entry_mao_obra = ctk.CTkEntry(frame, width=350, placeholder_text="Ex: 120.00", font=('Roboto', 14))
    entry_mao_obra.grid(row=3, column=1, sticky='w', pady=15, padx=(0, 20))

    label_info_os = ctk.CTkLabel(frame, text="", font=("Roboto", 10))
    label_info_os.place(x=150, y=55)

    label_peca = ctk.CTkLabel(frame, text="", font=("Roboto", 10))
    label_peca.place(x=150, y=126)
    label_peca.lift()

    label_valor_total_peca = ctk.CTkLabel(frame, text="", font=("Roboto", 10))
    label_valor_total_peca.place(x=150, y=183)


    def buscar_os(event=None):
        if not entry_id_os.get():
            label_info_os.configure(text=f'Informe a OS.', text_color="#ff5555")
        ordem = mostrar_uma_os(entry_id_os.get())

        if ordem:
            tecnico = mostrar_um_tecnico(ordem['id_tecnico'])
            label_info_os.configure(text=f"ID: {tecnico['id']} - Técnico: {tecnico['nome']}", text_color="#50fa7b")
    entry_id_os.bind("<KeyRelease>", buscar_os)

    def buscar_peca(event=None):
        if not entry_id_os.get():
            label_peca.configure(text=f'Informe uma peça.', text_color="#ff5555")

        id_peca = mostrar_uma_peca(entry_id_peca.get())

        if id_peca:
            label_peca.configure(text=f'Peça: {id_peca['nome']} - Valor UNI: {id_peca['preco']}', text_color="#50fa7b")
        else:
            label_peca.configure(text=f'Não encontrado', text_color="#ff5555")

    entry_id_peca.bind("<FocusOut>", buscar_peca)

    def total_valor_pecas(event=None):
        peca = mostrar_uma_peca(entry_id_peca.get())
        quantidade = (entry_quantidade.get())

        if peca:
            total = float(peca['preco']) * int(quantidade or 0)
            label_valor_total_peca.configure(text=f"Valor total: {total:.2f}", text_color="#50fa7b")
    entry_quantidade.bind("<KeyRelease>", total_valor_pecas)


            
    def definir_orcamento():
        id_os = entry_id_os.get()
        id_peca = entry_id_peca.get()
        id_quantidade = entry_id_os.get()

        if not id_os or not id_peca or not id_quantidade:
            label_aviso.configure(text='Preenhca todos os campos', text_color="#ff5555")

        resultado = abrir_orcamento(id_os, id_peca, id_quantidade)

        if resultado is not None:
            print('Orçamento enviado!')

            label_aviso.configure(text='Orçamento enviado com suecsso!', text_color="#50fa7b" )
            entry_id_os.delete(0, 'end')
            entry_id_peca.delete(0, 'end')
            entry_quantidade.delete(0, 'end')
            entry_mao_obra.delete(0, 'end')
            # entry_preco_uni.delete(0, 'end')

    buttom_confirmar_orcamento = ctk.CTkButton(frame, text='Confirmar', font=('Roboto', 20), text_color="#50fa7b", command=definir_orcamento)
    buttom_confirmar_orcamento.grid(row=4, column=1, padx=(180, 0))


    label_aviso = ctk.CTkLabel(frame, text="", font=('roboto', 30))
    label_aviso.grid(row=5, column=0)