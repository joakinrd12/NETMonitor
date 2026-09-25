import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("🎨 Tema Cyberpunk Neon")
    
    lbl_desc = ctk.CTkLabel(tarjeta, text="Aplica una paleta de colores futurista al dashboard.", font=ctk.CTkFont(size=11))
    lbl_desc.pack(anchor="w", padx=15, pady=(5, 10))
    
    btn_aplicar = ctk.CTkButton(
        tarjeta, 
        text="Aplicar Tema Cyberpunk", 
        fg_color="#b5179e", 
        hover_color="#7209b7", 
        command=lambda: aplicar_estilo_cyberpunk(app)
    )
    btn_aplicar.pack(anchor="w", padx=15, pady=10)

def aplicar_estilo_cyberpunk(app):
    try:
        # Cambiar el color de fondo de la ventana principal si lo soporta
        app.configure(fg_color="#0f0e17")
        
        print("[Tema] ¡Estilo Cyberpunk aplicado con éxito!")
    except Exception as e:
        print(f"[Error al aplicar tema]: {e}")