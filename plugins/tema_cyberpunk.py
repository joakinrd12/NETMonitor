import customtkinter as ctk
import tkinter as tk
import random

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🔴 HACKER PROTOCOL [THEME 2077]")
    
    ascii_logo = ">> SECURE_NET // CYBER_GRID_ACTIVE <<"
    lbl_ascii = ctk.CTkLabel(tarjeta, text=ascii_logo, text_color="#ff003c", font=ctk.CTkFont(family="Consolas", size=11, weight="bold"))
    lbl_ascii.pack(anchor="w", padx=15, pady=(5, 2))
    
    lbl_desc = ctk.CTkLabel(tarjeta, text="Genera un patrón de circuitos de red en el fondo y estilo 2077.", text_color="#a0a0a0", font=ctk.CTkFont(size=10))
    lbl_desc.pack(anchor="w", padx=15, pady=(0, 10))
    
    btn_aplicar = ctk.CTkButton(
        tarjeta, 
        text="⚡ Activar Interfaz Cyberpunk 2077", 
        fg_color="#cc0000", 
        hover_color="#ff1a1a", 
        text_color="#ffffff",
        command=lambda: aplicar_estilo_2077(app)
    )
    btn_aplicar.pack(anchor="w", padx=15, pady=10)

def aplicar_estilo_2077(app):
    try:
        # 1. Fondo principal de la ventana en negro profundo
        app.configure(fg_color="#08080c")
        
        # 2. Crear un fondo de circuitos digitales si no existe
        if not hasattr(app, "canvas_circuitos"):
            app.canvas_circuitos = tk.Canvas(app, bg="#08080c", highlightthickness=0)
            app.canvas_circuitos.place(x=0, y=0, relwidth=1, relheight=1)
            app.canvas_circuitos.lower() # Enviar detrás de todos los elementos
            
            w = app.winfo_width() or 1000
            h = app.winfo_height() or 700
            
            # Dibujar líneas de circuitos estilo placa madre / red cyberpunk en los espacios vacíos
            for _ in range(40):
                x1 = random.randint(30, w - 30)
                y1 = random.randint(30, h - 30)
                x2 = x1 + random.choice([-180, -100, -50, 50, 100, 180])
                y2 = y1
                x3 = x2
                y3 = y2 + random.choice([-120, -60, 60, 120])
                
                # Líneas de circuito en rojo oscuro de fondo
                app.canvas_circuitos.create_line(x1, y1, x2, y2, x3, y3, fill="#1f0208", width=2)
                # Nodos o puntos brillantes de conexión
                app.canvas_circuitos.create_oval(x1-2, y1-2, x1+2, y1+2, fill="#ff003c", outline="")
                app.canvas_circuitos.create_oval(x3-2, y3-2, x3+2, y3+2, fill="#ff003c", outline="")

        # 3. Recorrer widgets para estilizar tarjetas y actualizar botones con emojis 2077
        def actualizar_recursivo(widget):
            for hijo in widget.winfo_children():
                try:
                    if isinstance(hijo, ctk.CTkButton):
                        hijo.configure(
                            fg_color="#990000", 
                            hover_color="#ff0033", 
                            text_color="#ffffff"
                        )
                        # Agregar emojis y nomenclaturas según el botón
                        texto = hijo.cget("text")
                        if "Conexiones" in texto and "🔗" not in texto:
                            hijo.configure(text="🔗 Ver Conexiones [NET]")
                        elif "Escanear" in texto and "💻" not in texto:
                            hijo.configure(text="💻 Escanear Red [ARP]")
                        elif "Ping" in texto and "⚡" not in texto:
                            hijo.configure(text="⚡ Ejecutar Ping [ICMP]")
                            
                    elif isinstance(hijo, ctk.CTkFrame):
                        hijo.configure(
                            fg_color="#100e14", 
                            border_color="#550011", 
                            border_width=2
                        )
                except Exception:
                    pass
                
                actualizar_recursivo(hijo)

        actualizar_recursivo(app)
        print("[Tema 2077] ¡Circuitos de fondo y estilo completo aplicados con éxito!")
    except Exception as e:
        print(f"[Error aplicando tema 2077]: {e}")