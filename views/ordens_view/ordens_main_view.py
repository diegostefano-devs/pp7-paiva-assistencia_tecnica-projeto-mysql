import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import customtkinter as ctk
from views.ordens_view.ordens_view import abrir_os_view
from views.ordens_view.orcamento_os_view import orcamento_view
from views.ordens_view.finalizar_os_view import aprovar_orcamento
from views.ordens_view.ordens_listar_view import listar_ordens

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
frame_formulario.pack(fill='y',expand=True)

def apagar_formulario(frame):
    try:
        if frame.winfo_exists():
            for widget in frame.winfo_children():
                widget.destroy()
    except Exception:
        pass

def abrir_os():
    apagar_formulario(frame_formulario)
    abrir_os_view(frame_formulario)

def definir_orcamento():
    apagar_formulario(frame_formulario)
    orcamento_view(frame_formulario)

def aprovar_recusar_orcamento():
    apagar_formulario(frame_formulario)
    aprovar_orcamento(frame_formulario)
def mostrar_ordens_servico():
    apagar_formulario(frame_formulario)
    listar_ordens(frame_formulario)

bottom_abrir_os = ctk.CTkButton(frame_lateral, text='Abrir OS', font=("Roboto", 16, "bold"), command=abrir_os)
bottom_abrir_os.pack(pady=10, padx=20)
bottom_orcamento = ctk.CTkButton(frame_lateral, text='Orçamento', font=("Roboto", 16, "bold"), command=definir_orcamento)
bottom_orcamento.pack(pady=10, padx=20)
bottom_aprovar_recusar = ctk.CTkButton(frame_lateral, text='Aprovar/Recusar', font=("Roboto", 16, "bold"), command=aprovar_recusar_orcamento)
bottom_aprovar_recusar.pack(pady=10, padx=20)
bottom_mostrar = ctk.CTkButton(frame_lateral, text="Listar OS's", font=("Roboto", 16, "bold"), command=mostrar_ordens_servico)
bottom_mostrar.pack(pady=10, padx=20)
app.mainloop()