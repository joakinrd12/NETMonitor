import subprocess
import threading
import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🔌 Conexiones Activas")
    
    global lbl_estado_conn
    lbl_estado_conn = ctk.CTkLabel(tarjeta, text="● Estado: Inactivo", text_color="gray", font=ctk.CTkFont(size=12, weight="bold"))
    lbl_estado_conn.pack(anchor="w", padx=15, pady=2)
    
    global txt_conn
    txt_conn = ctk.CTkTextbox(tarjeta, width=400, height=120)
    txt_conn.pack(padx=15, pady=5)
    txt_conn.insert("0.0", "Haz clic para ver conexiones activas...")
    
    btn = ctk.CTkButton(tarjeta, text="Ver Conexiones", width=120, command=lambda: ejecutar_hilo_netstat())
    btn.pack(anchor="w", padx=15, pady=10)

def ejecutar_hilo_netstat():
    txt_conn.delete("0.0", "end")
    txt_conn.insert("0.0", "Obteniendo datos...")
    lbl_estado_conn.configure(text="● Consultando...", text_color="orange")
    hilo = threading.Thread(target=buscar_netstat)
    hilo.daemon = True
    hilo.start()

def buscar_netstat():
    try:
        resultado = subprocess.check_output("netstat -ano", shell=True, text=True, encoding="cp850")
        txt_conn.delete("0.0", "end")
        # Mostramos solo un resumen para no saturar la tarjeta pequeña
        txt_conn.insert("0.0", resultado[:350] + "\n...") 
        lbl_estado_conn.configure(text="● Datos Actualizados", text_color="green")
    except Exception as e:
        txt_conn.delete("0.0", "end")
        txt_conn.insert("0.0", f"Error: {e}")
        lbl_estado_conn.configure(text="● Error", text_color="red")