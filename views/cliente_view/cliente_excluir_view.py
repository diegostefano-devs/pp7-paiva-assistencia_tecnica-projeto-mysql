import customtkinter as ctk
from controllers.cliente_controller import excluir_cliente

cpf_excluir = None
lbl_aviso_exc = None

def exibir_tela_excluir(frame_centro):
    global cpf_excluir, lbl_aviso_exc
    
    for widget in frame_centro.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame_centro, 
        text="Excluir Cliente", 
        font=("Roboto", 18, "bold"), 
        text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(frame_centro, text="CPF do Cliente a Excluir:", font=("Roboto", 16), text_color="white").pack(pady=2)
    cpf_excluir = ctk.CTkEntry(frame_centro, font=("Roboto", 16), width=300)
    cpf_excluir.pack(pady=5)

    
    lbl_aviso_exc = ctk.CTkLabel(frame_centro, text="", font=("Roboto", 14, "bold"))
    lbl_aviso_exc.pack(pady=5)

    def excluir():    
        cpf = cpf_excluir.get()

        if not cpf:
            lbl_aviso_exc.configure(text="Digite o CPF do cliente!", text_color="#ef4444")
            return
        try:
            resultado = excluir_cliente(cpf)
            if resultado:
                lbl_aviso_exc.configure(text="Cliente excluído com sucesso!", text_color="#22c55e") 
                print(f"Excluindo cliente CPF: {cpf}")
            else:
                lbl_aviso_exc.configure(text="Cliente não cadastrado.", text_color="#ef4444") 

            cpf_excluir.delete(0, 'end')
            
        except Exception as erro:
            lbl_aviso_exc.configure(text="Esse cliente tem uma OS registrada e não pode ser apagado.", text_color="#ef4444")
            print(f"Erro: {erro}")
            
    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Exclusão", 
        font=("Roboto", 16, "bold"), 
        fg_color="#ef4444", 
        hover_color="#dc2626",
        text_color="white", 
        width=200,
        command=excluir
    ).pack(pady=15)