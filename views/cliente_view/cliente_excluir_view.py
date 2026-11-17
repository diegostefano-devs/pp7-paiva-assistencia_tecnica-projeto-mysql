import customtkinter as ctk

cpf_excluir = None

def exibir_tela_excluir(frame_centro):
    global cpf_excluir
    
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

    def excluir():
        print(f"Excluindo cliente CPF: {cpf_excluir.get()}")

    ctk.CTkButton(
        frame_centro, 
        text="Confirmar Exclusão", 
        font=("Roboto", 16, "bold"), 
        fg_color="#2196f3", 
        hover_color="#1976d2",
        text_color="white", 
        width=200,
        command=excluir
    ).pack(pady=20)