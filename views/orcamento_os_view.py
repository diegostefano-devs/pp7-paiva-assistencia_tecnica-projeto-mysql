import customtkinter as ctk
from controllers.itens_ordens_controller import abrir_orcamento
from controllers.peca_controllers import mostrar_uma_peca

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Orçamento')
app.geometry('1280x720')

label_titulo = ctk.CTkLabel(app, text='ORÇAMENTO', font=('Roboto', 30, 'bold')).grid(row=0, column=2,padx=(100, 0), pady=(10, 35))

for i, campo in enumerate(["ID da OS", "ID da Peça", "Quantidade", "Preço Unitário", "Mão de Obra"]):
    ctk.CTkLabel(app, text=f'{campo}:', font=("Robuto", 20, 'bold')).grid(row=i+1, column=1, sticky='w', pady=10, padx=(300, 0))

entry_id_os = ctk.CTkEntry(app, width=400, placeholder_text='Digite o ID da OS', font=('Roboto', 14))
entry_id_os.grid(row=1, column=2)

entry_id_peca = ctk.CTkEntry(app, width=400, placeholder_text='Digite o ID da Peça', font=('Roboto', 14))
entry_id_peca.grid(row=2, column=2)

entry_quantidade = ctk.CTkEntry(app, width=400, placeholder_text="Ex: 1", font=('Roboto', 14))
entry_quantidade.grid(row=3, column=2)

entry_preco_uni = ctk.CTkEntry(app, width=400, placeholder_text="Ex: 120.00", font=('Roboto', 14))
entry_preco_uni.grid(row=4, column=2)

entry_mao_obra = ctk.CTkEntry(app, width=400, placeholder_text="Ex: 120.00", font=('Roboto', 14))
entry_mao_obra.grid(row=5, column=2)

label_peca = ctk.CTkLabel(app, text="", font=("Roboto", 14))
label_peca.place(x=860, y=145)
label_peca.lift()


def buscar_peca(event=None):
    id_peca = mostrar_uma_peca(entry_id_peca.get())

    if id_peca:
        label_peca.configure(text=f'Peça: {id_peca['nome']} - Valor UNI: {id_peca['preco']}', text_color="#50fa7b")
    else:
        label_peca.configure(text=f'Não encontrado', text_color="#ff5555")

entry_id_peca.bind("<KeyRelease>", buscar_peca)

# def total_valor_pecas():
        
def abrir_orcamento():
    id_os = entry_id_os.get()
    id_peca = entry_id_peca.get()
    id_quantidade = entry_id_os.get()

    if not id_os or not id_peca or not id_quantidade:
        label_aviso.configure(text='Preenhca todos os campos', text_color="#ff5555")

    resultado = abrir_orcamento()

    if resultado is not None:
        print('Orçamento enviado!')

        label_aviso.configure(text='Orçamento enviado com suecsso!', text_color="#50fa7b" )
        entry_id_os.delete(0, 'end')
        entry_id_peca.delete(0, 'end')
        entry_quantidade.delete(0, 'end')
        entry_mao_obra.delete(0, 'end')
        # entry_preco_uni.delete(0, 'end')

buttom_confirmar_orcamento = ctk.CTkButton(app, text='Confirmar', font=('Roboto', 20), text_color="#50fa7b", command=abrir_orcamento)
buttom_confirmar_orcamento.grid(row=6, column=3, padx=(180, 0))


label_aviso = ctk.CTkLabel(app, text="", font=('roboto', 30))
label_aviso.grid(row=7, column=3)
app.mainloop()