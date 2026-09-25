import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🔴 HACKER PROTOCOL [THEME]")
    
    ascii_logo = ">> SECURE_NET // ACCESS_GRANTED <<"
    lbl_ascii = ctk.CTkLabel(tarjeta, text=ascii_logo, text_color="#ff003c", font=ctk.CTkFont(family="Consolas", size=11, weight="bold"))
    lbl_ascii.pack(anchor="w", padx=15, pady=(5, 2))
    
    lbl_desc = ctk.CTkLabel(tarjeta, text="Inspirado en la estación de comando: negros profundos y rojo carmesí.", text_color="#a0a0a0", font=ctk.CTkFont(size=10))
    lbl_desc.pack(anchor="w", padx=15, pady=(0, 10))
    
    btn_aplicar = ctk.CTkButton(
        tarjeta, 
        text="⚡ Forzar Protocolo Hacker Total", 
        fg_color="#cc0000", 
        hover_color="#ff1a1a", 
        text_color="#ffffff",
        command=lambda: aplicar_estilo_total(app)
    )
    btn_aplicar.pack(anchor="w", padx=15, pady=10)

def aplicar_estilo_total(app):
    try:
        # 1. Fondo principal de la ventana (Negro estación de hacking)
        app.configure(fg_color="#08080c")
        
        # 2. Función recursiva para cambiar TODO en la interfaz dinámicamente
        def actualizar_recursivo(widget):
            for hijo in widget.winfo_children():
                try:
                    # Si es un botón, lo ponemos en rojo hacker brillante
                    if isinstance(hijo, ctk.CTkButton):
                        hijo.configure(
                            fg_color="#990000", 
                            hover_color="#ff0033", 
                            text_color="#ffffff"
                        )
                    # Si es un contenedor o tarjeta (Frame), oscurecemos el fondo y añadimos un borde sutil rojizo
                    elif isinstance(hijo, ctk.CTkFrame):
                        hijo.configure(
                            fg_color="#12131a", 
                            border_color="#400000", 
                            border_width=2
                        )
                except Exception:
                    pass
                
                # Continuar buscando dentro de los hijos (recursividad)
                actualizar_recursivo(hijo)

        # Aplicar el cambio a toda la app
        actualizar_recursivo(app)
        print("[Tema Total] ¡Interfaz convertida al estilo Hacker con éxito!")
    except Exception as e:
        print(f"[Error al aplicar el tema total]: {e}")