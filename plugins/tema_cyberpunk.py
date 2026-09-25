import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🔴 HACKER PROTOCOL [THEME]")
    
    # Texto con estilo terminal de hacking
    ascii_logo = ">> SECURE_NET // ACCESS_GRANTED <<"
    lbl_ascii = ctk.CTkLabel(tarjeta, text=ascii_logo, text_color="#ff003c", font=ctk.CTkFont(family="Consolas", size=11, weight="bold"))
    lbl_ascii.pack(anchor="w", padx=15, pady=(5, 2))
    
    lbl_desc = ctk.CTkLabel(tarjeta, text="Paleta inspirada en estaciones de comando oscuras y alertas rojas.", text_color="#a0a0a0", font=ctk.CTkFont(size=10))
    lbl_desc.pack(anchor="w", padx=15, pady=(0, 10))
    
    btn_aplicar = ctk.CTkButton(
        tarjeta, 
        text="⚡ Activar Protocolo Oscuro", 
        fg_color="#8b0000", 
        hover_color="#ff003c", 
        text_color="#ffffff",
        command=lambda: aplicar_estilo_hacker(app)
    )
    btn_aplicar.pack(anchor="w", padx=15, pady=10)

def aplicar_estilo_hacker(app):
    try:
        # Fondo general de la app en un gris muy oscuro (como el entorno de la imagen)
        app.configure(fg_color="#0d0d0d")
        
        # Cambiar el modo de apariencia global a Oscuro
        ctk.set_appearance_mode("Dark")
        
        print("[Tema] ¡Protocolo Hacker / Rojo Neón aplicado con éxito!")
    except Exception as e:
        print(f"[Error al aplicar tema hacker]: {e}")