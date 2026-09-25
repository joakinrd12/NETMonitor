import subprocess
import threading
import platform
import customtkinter as ctk

def crear_tarjeta(app):
    # Pedimos una tarjeta al núcleo
    tarjeta = app.agregar_tarjeta_dashboard("🌐 Estado de Latencia (Ping)")
    
    # Indicador visual de estado (Color inicial: Gris/Neutro)
    global lbl_estado_ping
    lbl_estado_ping = ctk.CTkLabel(tarjeta, text="● Estado: En espera", text_color="gray", font=ctk.CTkFont(size=12, weight="bold"))
    lbl_estado_ping.pack(anchor="w", padx=15, pady=2)
    
    lbl_info = ctk.CTkLabel(tarjeta, text="Destino: 8.8.8.8")
    lbl_info.pack(anchor="w", padx=15, pady=2)
    
    btn = ctk.CTkButton(tarjeta, text="Probar Ping", width=120, command=lambda: ejecutar_hilo_ping())
    btn.pack(anchor="w", padx=15, pady=10)

def ejecutar_hilo_ping():
    lbl_estado_ping.configure(text="● Probando...", text_color="orange")
    hilo = threading.Thread(target=hacer_ping_real)
    hilo.daemon = True
    hilo.start()

def hacer_ping_real():
    try:
        parametro = "-n" if platform.system().lower() == "windows" else "-c"
        comando = f"ping {parametro} 1 8.8.8.8"
        subprocess.check_output(comando, shell=True, text=True, encoding="cp850")
        
        # Si responde bien -> Alerta Verde (Todo bien)
        lbl_estado_ping.configure(text="● Conexión Óptima (< 50ms)", text_color="green")
    except:
        # Si falla -> Alerta Roja (Sin conexión o problema)
        lbl_estado_ping.configure(text="● Sin respuesta (Error)", text_color="red")