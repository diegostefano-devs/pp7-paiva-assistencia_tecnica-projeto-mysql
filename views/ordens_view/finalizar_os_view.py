from functools import partial

import customtkinter as ctk
from controllers.ordens_controller import listar_todas_os, mostrar_uma_os, finalizar_ordem_de_servico
from controllers.tecnico_controllers import mostrar_um_tecnico
from controllers.cliente_controller import mostrar_um_cliente

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Ordens de Serviço')
app.geometry('800x600')

faixa = ctk.CTkFrame(app, fg_color="#2d2853", height=90)
faixa.pack(side=ctk.TOP, fill=ctk.X)

titulo = ctk.CTkLabel(faixa, text="Ordens de Serviço", font=("Roboto", 30, 'bold')).pack(pady=24)

frame_lateral = ctk.CTkFrame(app, fg_color="#2b2b2b", width=200, corner_radius=0)
frame_lateral.pack(side="left", fill=ctk.Y)

frame_centro = ctk.CTkFrame(app, fg_color="#1a1a1a")
frame_centro.pack(side="right", expand=True, fill=ctk.BOTH)

frame_formulario = ctk.CTkFrame(frame_centro, fg_color="transparent")
frame_formulario.pack(fill="x", padx=20, pady=40, anchor="n")


label_os_info = ctk.CTkLabel(frame_formulario, text=f"ID da OS: ", font=("Roboto", 16))
label_os_info.grid(row=0, column=0, sticky='w', pady=15, padx=(50,20))

entry_id_os = ctk.CTkEntry(frame_formulario, placeholder_text='Exemplo: 1', font=('Roboto', 14, 'bold'))
entry_id_os.grid(row=0, column=1, sticky='w', pady=15)

label_info_geral = ctk.CTkLabel(frame_centro, text='', font=('Roboto', 20, 'bold'), justify='left')
label_info_geral.place(x=70, y=140)

label_aviso = ctk.CTkLabel(frame_centro, text="", font=('roboto', 12))
label_aviso.place(x=80, y=85)

def chamar_os(event, id_os, aviso):
    if not id_os.get():
        aviso.configure(text=f'Informe a OS.', text_color="#ff5555")
        return
    ordem = mostrar_uma_os(id_os.get())

    if not ordem: 
        aviso.configure(text="OS não encontrada.", text_color="#ff5555")
        return

    try:
        total_orcamento = ordem['valor_fixo'] + ordem['valor_total']
        if total_orcamento == 0:
            aviso.configure(text="OS sem orçamento.", text_color="#ff5555")
            return
        tecnico = mostrar_um_tecnico(ordem['id_tecnico'])
        cliente = mostrar_um_cliente(ordem['id_cliente'])
        aviso.configure(
                text=f"Cliente: {cliente['nome']} --- Técnico: {tecnico['nome']}\nAparelho: {ordem['aparelho']}\nValor Fixo (Mão de Obra): {ordem['valor_fixo']}\nValor Total: {total_orcamento}", text_color="#50fa7b")

    except Exception:
        aviso.configure(text="OS sem orçamento.", text_color="#ff5555")
        
entry_id_os.bind("<KeyRelease>", partial(chamar_os, id_os=entry_id_os, aviso=label_info_geral))

def confirmar_os(status, mensagem):
    id_os = entry_id_os.get()

    if not id_os:
        label_aviso.configure(text="Informe o ID da OS", text_color="#ff5555")

    resultado = finalizar_ordem_de_servico(id_os, status)
    if resultado is not None:

        label_aviso.configure(mensagem)
        entry_id_os.delete(0, 'end')
    else:
        label_aviso.configure(text="Erro ao realizar ação! Verifique o ID da OS.", text_color="#ff5555")

def recusar_orcamento():
    id_os = entry_id_os.get()
    if not id_os:
        label_aviso.configure(text="Informe o ID da OS", text_color="#ff5555")

    resultado = finalizar_ordem_de_servico(id_os, "Orçamento Recusado")

    if resultado is not None:
        label_aviso.configure('Recusado')
        entry_id_os.delete(0, 'end')
    else:
        label_aviso.configure(text="Erro ao realizar ação! Verifique o ID da OS.", text_color="#ff5555")



bottom_confirmar = ctk.CTkButton(frame_centro, text='Confirmar', command=lambda: confirmar_os("Em Manuntenção", "Orçamento aprovado!"))
bottom_confirmar.place(x=450, y=280)

bottom_recusar = ctk.CTkButton(frame_centro, text='Recusar', fg_color="#e46e6e", hover_color="#9b3f3f", command=lambda: confirmar_os("Orçamento Recusado", "Orçamento Recusado!"))
bottom_recusar.place(x=290, y=280)


app.mainloop()