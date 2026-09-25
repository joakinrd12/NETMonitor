import subprocess
import threading
import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("💻 Dispositivos en Red (ARP)")
    
    global lbl_estado_arp
    lbl_estado_arp = ctk.CTkLabel(tarjeta, text="● Red Local Detectada", text_color="green", font=ctk.CTkFont(size=12, weight="bold"))
    lbl_estado_arp.pack(anchor="w", padx=15, pady=2)
    
    global txt_resumen
    txt_resumen = ctk.CTkTextbox(tarjeta, width=400, height=120)
    txt_resumen.pack(padx=15, pady=5)
    txt_resumen.insert("0.0", "Haz clic para buscar equipos conectados...")
    
    btn = ctk.CTkButton(tarjeta, text="Escanear Ahora", width=120, command=lambda: ejecutar_hilo_arp())
    btn.pack(anchor="w", padx=15, pady=10)

def ejecutar_hilo_arp():
    txt_resumen.delete("0.0", "end")
    txt_resumen.insert("0.0", "Escaneando...")
    hilo = threading.Thread(target=buscar_arp)
    hilo.daemon = True
    hilo.start()

def buscar_arp():
    try:
        resultado = subprocess.check_output("arp -a", shell=True, text=True, encoding="cp850")
        txt_resumen.delete("0.0", "end")
        txt_resumen.insert("0.0", resultado[:300] + "\n...") # Mostramos un resumen limpio
        lbl_estado_arp.configure(text="● Escaneo Exitoso", text_color="green")
    except Exception as e:
        txt_resumen.delete("0.0", "end")
        txt_resumen.insert("0.0", f"Error: {e}")
        lbl_estado_arp.configure(text="● Error de red", text_color="red")