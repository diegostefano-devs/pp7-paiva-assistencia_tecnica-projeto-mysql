from functools import partial

import customtkinter as ctk
from controllers.ordens_controller import listar_todas_os, mostrar_uma_os, finalizar_ordem_de_servico
from controllers.tecnico_controllers import mostrar_um_tecnico
from controllers.cliente_controller import mostrar_um_cliente

# ctk.set_appearance_mode('dark')

# app = ctk.CTk()
# app.title('Ordens de Serviço')
# app.geometry('800x600')

# faixa = ctk.CTkFrame(app, fg_color="#2d2853", height=90)
# faixa.pack(side=ctk.TOP, fill=ctk.X)

# titulo = ctk.CTkLabel(faixa, text="Ordens de Serviço", font=("Roboto", 30, 'bold')).pack(pady=24)

# frame_lateral = ctk.CTkFrame(app, fg_color="#2b2b2b", width=200, corner_radius=0)
# frame_lateral.pack(side="left", fill=ctk.Y)

# frame_centro = ctk.CTkFrame(app, fg_color="#1a1a1a")
# frame_centro.pack(side="right", expand=True, fill=ctk.BOTH)

# frame_formulario = ctk.CTkFrame(frame_centro, fg_color="transparent")
# frame_formulario.pack(expand=True)

def aprovar_orcamento(frame_formulario):
    # Faz o frame_formulario ocupar todo o espaço do frame_centro,
    # assim as posições (place) ficam idênticas às de antes.
    frame_formulario.pack_configure(fill=ctk.BOTH, expand=True)

    label_os_info = ctk.CTkLabel(frame_formulario, text=f"ID da OS: ", font=("Roboto", 16))
    label_os_info.place(x=80, y=75)

    entry_id_os = ctk.CTkEntry(frame_formulario, placeholder_text='Exemplo: 1', font=('Roboto', 14, 'bold'))
    entry_id_os.place(x=168, y=75)

    label_info_geral = ctk.CTkLabel(frame_formulario, text='', font=('Roboto', 20, 'bold'), justify='left')
    label_info_geral.place(x=70, y=140)

    label_aviso = ctk.CTkLabel(frame_formulario, text="", font=('roboto', 12))
    label_aviso.place(x=80, y=105)

    def chamar_os(event, id_os, aviso):
        if not id_os.get():
            aviso.configure(text=f'Informe a OS.', text_color="#ff5555")
            return
        ordem = mostrar_uma_os(id_os.get())

        if not ordem: 
            aviso.configure(text="OS não encontrada.", text_color="#ff5555")
            return

        total_orcamento = ordem['valor_fixo'] + ordem['valor_total']

        tecnico = mostrar_um_tecnico(ordem['id_tecnico'])
        cliente = mostrar_um_cliente(ordem['id_cliente'])
        aviso.configure(
                    text=f"Cliente: {cliente['nome']} --- Técnico: {tecnico['nome']}\nAparelho: {ordem['aparelho']}\nValor Fixo (Mão de Obra): {ordem['valor_fixo']}\nValor Total (Peça e Mão de Obra): {total_orcamento}", text_color="#50fa7b")
            
    entry_id_os.bind("<KeyRelease>", partial(chamar_os, id_os=entry_id_os, aviso=label_info_geral))

    def confirmar_os(status, mensagem):
        id_os = entry_id_os.get()

        if not id_os:
            label_aviso.configure(text="Informe o ID da OS", text_color="#ff5555")
            return

        id_os = entry_id_os.get()

        if not id_os:
            label_aviso.configure(text="Informe o ID da OS", text_color="#ff5555")
            return

        try:
            finalizar_ordem_de_servico(id_os, status)
            
            label_aviso.configure(text=mensagem, text_color="#50fa7b")
            entry_id_os.delete(0, 'end')
            
        except ValueError as erro:
            label_aviso.configure(text=str(erro), text_color="#ff5555")
            
        except Exception as erro:
            label_aviso.configure(text=f"Erro: {erro}", text_color="#ff5555")   

    bottom_confirmar = ctk.CTkButton(frame_formulario, text='Confirmar', command=lambda: confirmar_os("EM MANUTENÇÃO", "Orçamento aprovado!"))
    bottom_confirmar.place(x=400, y=280)

    bottom_recusar = ctk.CTkButton(frame_formulario, text='Recusar', fg_color="#e46e6e", hover_color="#9b3f3f", command=lambda: confirmar_os("ORÇAMENTO NEGADO", "Orçamento Recusado!"))
    bottom_recusar.place(x=250, y=280)


# app.mainloop()