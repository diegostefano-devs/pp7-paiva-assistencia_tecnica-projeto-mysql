import customtkinter as ctk
from controllers.ordens_controller import listar_todas_os
from controllers.cliente_controller import mostrar_um_cliente
from controllers.tecnico_controllers import mostrar_um_tecnico

# ctk.set_appearance_mode('dark')

# app = ctk.CTk()
# app.title('Ordens de Serviço')
# app.geometry('800x600')

# Cabeçalho
# faixa = ctk.CTkFrame(app, fg_color="#2d2853", height=90)
# faixa.pack(side=ctk.TOP, fill=ctk.X)

# titulo = ctk.CTkLabel(faixa, text="Ordens de Serviço", font=("Roboto", 30, 'bold'))
# titulo.pack(pady=24)

# frame_lateral = ctk.CTkFrame(app, fg_color="#2b2b2b", width=200, corner_radius=0)
# frame_lateral.pack(side="left", fill=ctk.Y)

# frame_centro = ctk.CTkFrame(app, fg_color="#1a1a1a")
# frame_centro.pack(side="right", expand=True, fill=ctk.BOTH)

def listar_ordens(frame_c):
    frame_filtros = ctk.CTkFrame(frame_c, fg_color="transparent")
    frame_filtros.pack(side='top', fill='x', padx=20, pady=15)

    scroll_frame = ctk.CTkScrollableFrame(frame_c, fg_color="transparent")
    scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)

    var_orcamento = ctk.IntVar(value=1)
    var_aprovacao = ctk.IntVar(value=1)
    var_aprovadas = ctk.IntVar(value=1)
    var_recusadas = ctk.IntVar(value=1)
    var_finalizadas = ctk.IntVar(value=1)

    def chamar_dados():
        dados_os = listar_todas_os()

        for widget in scroll_frame.winfo_children():
            widget.destroy()    

        if dados_os:
            for os in dados_os:
                status = os['status']
                if status == "AGUARDANDO ORÇAMENTO" and not var_orcamento.get():
                    continue
                if status == "AGUARDANDO APROVAÇÃO" and not var_aprovacao.get():
                    continue
                if status == "EM MANUTENÇÃO" and not var_aprovadas.get():
                    continue
                if status == "ORÇAMENTO NEGADO" and not var_recusadas.get():
                    continue
                if status == "FINALIZADA" and not var_finalizadas.get():
                    continue

                cliente = mostrar_um_cliente(os['id_cliente'])
                tecnico = mostrar_um_tecnico(os['id_tecnico'])
                texto = f"OS: Nª{os['id']} | ID/Cliente: {os['id_cliente']} {cliente['nome']} | ID/Técnico: {os['id_tecnico']} {tecnico['nome']} | Status: {os['status']}"

                linha = ctk.CTkFrame(scroll_frame, fg_color="#2b2b2b", height=45)
                linha.pack(fill="x", pady=5)

                label = ctk.CTkLabel(linha, text=texto, font=('Roboto', 13))
                label.pack(side="left", padx=15, pady=10)


    check_status_orcamento = ctk.CTkCheckBox(frame_filtros, text='Aguardando Orçamento', variable=var_orcamento, command=chamar_dados)
    check_status_orcamento.pack(side='left', padx=(0, 15))

    check_status_aprovacao = ctk.CTkCheckBox(frame_filtros, text='Aguardando Aprovação', variable=var_aprovacao, command=chamar_dados)
    check_status_aprovacao.pack(side='left', padx=(0, 15))

    check_status_aprovadas = ctk.CTkCheckBox(frame_filtros, text='Em Manuntenção', variable=var_aprovadas, command=chamar_dados)
    check_status_aprovadas.pack(side='left', padx=(0,15))

    check_status_recusdas = ctk.CTkCheckBox(frame_filtros, text='Recusadas', variable=var_recusadas, command=chamar_dados)
    check_status_recusdas.pack(side='left', padx=(0,15))

    check_status_finalizadas = ctk.CTkCheckBox(frame_filtros, text='Finalizadas', variable=var_finalizadas, command=chamar_dados)
    check_status_finalizadas.pack(side='left', padx=(0,15))

    chamar_dados()         



# app.mainloop()