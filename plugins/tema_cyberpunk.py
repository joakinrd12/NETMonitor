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
        command=lambda: aplicar_estilo_cyberpunk()
    )
    btn_aplicar.pack(anchor="w", padx=15, pady=10)

def aplicar_estilo_cyberpunk():
    # Cambiamos los colores generales de CustomTkinter en tiempo de ejecución
    ctk.set_appearance_mode("Dark")
    # CustomTkinter permite cambiar el color por defecto de los elementos interactivos
    ctk.set_default_color_theme("dark-blue")
    print("[Tema] ¡Estilo Cyberpunk aplicado con éxito!")