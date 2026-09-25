import os
import json
import urllib.request
import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("📦 Gestor de Paquetes (Tienda)")
    
    global lbl_estado_gp
    lbl_estado_gp = ctk.CTkLabel(tarjeta, text="● Estado: Listo para buscar actualizaciones", text_color="green", font=ctk.CTkFont(size=11, weight="bold"))
    lbl_estado_gp.pack(anchor="w", padx=15, pady=2)
    
    # Cuadro de texto para mostrar los plugins disponibles en el registry
    global txt_disponibles
    txt_disponibles = ctk.CTkTextbox(tarjeta, width=400, height=90)
    txt_disponibles.pack(padx=15, pady=5)
    
    # Cargar la lista al iniciar la tarjeta
    cargar_catalogo()
    
    # Botón para instalar el gráfico de latencia de prueba
    btn_instalar = ctk.CTkButton(tarjeta, text="Instalar Gráfico de Latencia", fg_color="#2b8a3e", hover_color="#2b7034", command=lambda: instalar_plugin("grafico_latencia"))
    btn_instalar.pack(anchor="w", padx=15, pady=10)

def cargar_catalogo():
    try:
        # Leer el registry.json local
        if os.path.exists("registry.json"):
            with open("registry.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
            txt_disponibles.delete("0.0", "end")
            texto_catalogo = "Plugins disponibles en el repositorio:\n\n"
            for p in data.get("plugins_disponibles", []):
                texto_catalogo += f"• {p['nombre']}: {p['descripcion']}\n"
            txt_disponibles.insert("0.0", texto_catalogo)
        else:
            txt_disponibles.delete("0.0", "end")
            txt_disponibles.insert("0.0", "No se encontró el archivo registry.json en la raíz.")
    except Exception as e:
        txt_disponibles.delete("0.0", "end")
        txt_disponibles.insert("0.0", f"Error leyendo el registro: {e}")

def instalar_plugin(nombre_plugin):
    try:
        lbl_estado_gp.configure(text=f"● Descargando {nombre_plugin}...", text_color="orange")
        
        # Leer el link de descarga desde el registry.json
        with open("registry.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        url_a_descargar = ""
        archivo_destino = ""
        for p in data.get("plugins_disponibles", []):
            if p["nombre"] == nombre_plugin:
                url_a_descargar = p["url_descarga"]
                archivo_destino = os.path.join("plugins", p["archivo"])
                break
                
        if not url_a_descargar:
            lbl_estado_gp.configure(text="● Error: Plugin no encontrado en el registro", text_color="red")
            return
            
        # Descargar el archivo usando urllib (nativo de Python)
        urllib.request.urlretrieve(url_a_descargar, archivo_destino)
        
        lbl_estado_gp.configure(text=f"● ¡Instalado con éxito! Reinicia la app.", text_color="green")
        
    except Exception as e:
        lbl_estado_gp.configure(text=f"● Error al instalar: {e}", text_color="red")