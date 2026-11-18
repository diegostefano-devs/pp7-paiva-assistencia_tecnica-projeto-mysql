import customtkinter as ctk
# Importa a função do controller que busca os técnicos cadastrados no MySQL
from controllers.tecnico_controllers import tecnico

def exibir_tela_listar(frame_centro):
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Lista de Técnicos Cadastrados", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    # Frame com rolagem para exibir os técnicos
    frame_lista = ctk.CTkScrollableFrame(frame_centro, fg_color="#212121", width=500, height=350)
    frame_lista.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)

    try:
        # Puxa os dados reais do banco através do controller
        lista_tecnicos = tecnico()

        if not lista_tecnicos:
            ctk.CTkLabel(
                frame_lista, 
                text="Nenhum técnico cadastrado no momento.", 
                font=("Roboto", 14), 
                text_color="gray"
            ).pack(pady=20)
        else:
            # Percorre os técnicos vindos do banco e cria um card para cada um
            for tec in lista_tecnicos:
                card = ctk.CTkFrame(frame_lista, fg_color="#2b2b2b", corner_radius=6)
                card.pack(fill=ctk.X, pady=5, padx=5)

                # Compatibilidade caso venha em dicionário ou tupla
                if isinstance(tec, dict):
                    nome = tec.get('nome')
                    cpf = tec.get('cpf')
                    telefone = tec.get('telefone')
                else:
                    # Ajuste a ordem dos índices (ex: [0]=cpf, [1]=nome, [2]=telefone) conforme sua tupla do banco
                    cpf = tec[0]
                    nome = tec[1]
                    telefone = tec[2]

                texto_info = f"Nome: {nome}  |  CPF: {cpf}  |  Tel: {telefone}"
                ctk.CTkLabel(
                    card, 
                    text=texto_info, 
                    font=("Roboto", 14), 
                    text_color="white"
                ).pack(side=ctk.LEFT, padx=15, pady=10)

    except Exception as erro:
        ctk.CTkLabel(
            frame_lista, 
            text=f"Erro ao carregar técnicos: {erro}", 
            font=("Roboto", 14), 
            text_color="#ef4444"
        ).pack(pady=20)