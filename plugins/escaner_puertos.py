import customtkinter as ctk
import socket
import threading

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🔍 Escáner de Puertos [TCP]")
    
    lbl_info = ctk.CTkLabel(tarjeta, text="Analiza puertos críticos en una IP de destino", font=ctk.CTkFont(size=10), text_color="#a0a0a0")
    lbl_info.pack(anchor="w", padx=15, pady=(5, 2))
    
    # Campo de entrada para la IP objetivo
    global entry_ip
    entry_ip = ctk.CTkEntry(tarjeta, placeholder_text="Ej: 192.168.1.1 o 8.8.8.8", width=220, fg_color="#08080c", border_color="#550011")
    entry_ip.pack(anchor="w", padx=15, pady=5)
    
    # Cuadro de texto para los resultados
    global txt_resultados_puertos
    txt_resultados_puertos = ctk.CTkTextbox(tarjeta, width=420, height=100, fg_color="#08080c", text_color="#00ff66")
    txt_resultados_puertos.pack(padx=15, pady=5)
    
    btn_escanear = ctk.CTkButton(
        tarjeta, 
        text="⚡ Iniciar Escaneo de Puertos", 
        fg_color="#990000", 
        hover_color="#ff0033",
        height=28,
        command=lambda: iniciar_hilo_escaneo()
    )
    btn_escanear.pack(anchor="w", padx=15, pady=8)

def iniciar_hilo_escaneo():
    ip_objetivo = entry_ip.get().strip()
    if not ip_objetivo:
        txt_resultados_puertos.delete("0.0", "end")
        txt_resultados_puertos.insert("0.0", "[!] Error: Ingresa una dirección IP válida.")
        return
        
    txt_resultados_puertos.delete("0.0", "end")
    txt_resultados_puertos.insert("0.0", f"[*] Escaneando puertos en {ip_objetivo}...\n")
    
    # Ejecutar en segundo plano para no congelar la interfaz gráfica
    hilo = threading.Thread(target=escanear_puertos, args=(ip_objetivo,))
    hilo.daemon = True
    hilo.start()

def escanear_puertos(ip):
    # Puertos comunes a escanear (FTP, SSH, HTTP, HTTPS, RDP, etc.)
    puertos_comunes = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3389: "RDP (Escritorio Remoto)",
        8080: "HTTP-Proxy"
    }
    
    resultados = f"[*] Analizando {ip}...\n"
    
    for puerto, servicio in puertos_comunes.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            resultado = s.connect_ex((ip, puerto))
            s.close()
            
            if resultado == 0:
                resultados += f"[ABIERTO] Puerto {puerto} ({servicio})\n"
            else:
                resultados += f"[CERRADO] Puerto {puerto} ({servicio})\n"
        except Exception as e:
            resultados += f"[ERROR] Puerto {puerto}: {e}\n"
            
    resultados += "\n[+] Escaneo de puertos finalizado."
    
    # Actualizar la interfaz de manera segura desde el hilo
    txt_resultados_puertos.delete("0.0", "end")
    txt_resultados_puertos.insert("0.0", resultados)