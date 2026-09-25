import customtkinter as ctk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("📈 Gráfico de Latencia en Vivo")
    
    lbl_info = ctk.CTkLabel(tarjeta, text="Monitoreo ICMP en tiempo real con control de pausa", font=ctk.CTkFont(size=10), text_color="#a0a0a0")
    lbl_info.pack(anchor="w", padx=15, pady=(5, 5))
    
    # Crear figura de Matplotlib con estética oscura
    fig = Figure(figsize=(4, 2), dpi=80)
    fig.patch.set_facecolor('#100e14')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#08080c')
    
    # Datos iniciales
    tiempos = list(range(10))
    latencias = [random.randint(15, 45) for _ in range(10)]
    
    linea, = ax.plot(tiempos, latencias, color='#ff003c', linewidth=2, marker='o', markersize=4)
    ax.set_title("Latencia (ms)", color='#ffffff', fontsize=9)
    ax.tick_params(colors='#a0a0a0', labelsize=8)
    ax.spines['bottom'].set_color('#550011')
    ax.spines['top'].set_color('#100e14')
    ax.spines['left'].set_color('#550011')
    ax.spines['right'].set_color('#100e14')
    
    canvas = FigureCanvasTkAgg(fig, master=tarjeta)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=5, fill="both", expand=True)
    
    # Diccionario de estado para manejar la pausa
    control_estado = {"pausado": False}
    
    # Función que actualiza el gráfico automáticamente cada 2 segundos
    def bucle_tiempo_real():
        if not control_estado["pausado"]:
            nuevas_latencias = latencias[1:] + [random.randint(12, 80)]
            latencias.clear()
            latencias.extend(nuevas_latencias)
            linea.set_ydata(latencias)
            ax.relim()
            ax.autoscale_view()
            canvas.draw()
        
        # Repetir el ciclo de actualización
        tarjeta.after(2000, bucle_tiempo_real)
        
    def toggle_pausa():
        control_estado["pausado"] = not control_estado["pausado"]
        if control_estado["pausado"]:
            btn_pausa.configure(text="▶️ Reanudar (En Vivo)", fg_color="#b8860b", hover_color="#daa520")
        else:
            btn_pausa.configure(text="⏸️ Pausar", fg_color="#990000", hover_color="#ff0033")

    # Botón de control de Pausa/Tiempo Real
    btn_pausa = ctk.CTkButton(
        tarjeta, 
        text="⏸️ Pausar", 
        fg_color="#990000", 
        hover_color="#ff0033",
        height=26,
        width=130,
        command=toggle_pausa
    )
    btn_pausa.pack(anchor="w", padx=15, pady=8)
    
    # Iniciar el bucle en segundo plano dentro de la app
    bucle_tiempo_real()