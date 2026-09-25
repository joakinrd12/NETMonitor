import customtkinter as ctk
import subprocess
import platform
import threading

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🗺️ Rastreador de Rutas [Traceroute]")
    
    lbl_info = ctk.CTkLabel(tarjeta, text="Rastrea los saltos de red hacia un destino IP o dominio", font=ctk.CTkFont(size=10), text_color="#a0a0a0")
    lbl_info.pack(anchor="w", padx=15, pady=(5, 2))
    
    global entry_trace_ip
    entry_trace_ip = ctk.CTkEntry(tarjeta, placeholder_text="Ej: google.com o 1.1.1.1", width=220, fg_color="#08080c", border_color="#550011")
    entry_trace_ip.pack(anchor="w", padx=15, pady=5)
    
    global txt_resultados_trace
    txt_resultados_trace = ctk.CTkTextbox(tarjeta, width=420, height=100, fg_color="#08080c", text_color="#00ff66")
    txt_resultados_trace.pack(padx=15, pady=5)
    
    btn_trace = ctk.CTkButton(
        tarjeta, 
        text="⚡ Rastrear Saltos [PATH]", 
        fg_color="#990000", 
        hover_color="#ff0033",
        height=28,
        command=lambda: iniciar_hilo_traceroute()
    )
    btn_trace.pack(anchor="w", padx=15, pady=8)

def iniciar_hilo_traceroute():
    destino = entry_trace_ip.get().strip()
    if not destino:
        txt_resultados_trace.delete("0.0", "end")
        txt_resultados_trace.insert("0.0", "[!] Error: Ingresa un destino válido.")
        return
        
    txt_resultados_trace.delete("0.0", "end")
    txt_resultados_trace.insert("0.0", f"[*] Analizando ruta de saltos hacia {destino}...\n")
    
    hilo = threading.Thread(target=ejecutar_traceroute, args=(destino,))
    hilo.daemon = True
    hilo.start()

def ejecutar_traceroute(destino):
    # Detectar el sistema operativo para usar el comando correcto (tracert en Windows, traceroute en Linux/Mac)
    parametro_so = "-n" if platform.system().lower() == "windows" else "-m"
    comando = "tracert" if platform.system().lower() == "windows" else "traceroute"
    
    try:
        proceso = subprocess.Popen([comando, parametro_so, destino], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida, error = proceso.communicate(timeout=30)
        
        if proceso.returncode == 0 or salida:
            resultado_final = f"[*] Ruta completada a {destino}:\n\n" + salida
        else:
            resultado_final = f"[!] Error en el rastreo: {error}"
            
    except subprocess.TimeoutExpired:
        resultado_final = "[!] El tiempo de espera del comando expiró."
    except Exception as e:
        resultado_final = f"[!] Error crítico: {e}"
        
    txt_resultados_trace.delete("0.0", "end")
    txt_resultados_trace.insert("0.0", resultado_final)