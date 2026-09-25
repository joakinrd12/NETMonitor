import os
import json
import urllib.request
import urllib.error
import customtkinter as ctk

def crear_tarjeta(app):
    tarjeta = app.agregar_tarjeta_dashboard("📦 Gestor de Paquetes (Tienda)")
    
    global lbl_estado_gp, frame_plugins
    lbl_estado_gp = ctk.CTkLabel(tarjeta, text="● Estado: Catálogo sincronizado", text_color="#00ff66", font=ctk.CTkFont(size=11, weight="bold"))
    lbl_estado_gp.pack(anchor="w", padx=15, pady=2)
    
    # Contenedor donde se listarán dinámicamente los plugins disponibles
    frame_plugins = ctk.CTkScrollableFrame(tarjeta, width=420, height=140, fg_color="#100e14")
    frame_plugins.pack(padx=15, pady=5)
    
    # Cargar el catálogo dinámico
    cargar_catalogo()

def cargar_catalogo():
    # Limpiar frame por si se recarga
    for widget in frame_plugins.winfo_children():
        widget.destroy()
        
    try:
        if os.path.exists("registry.json"):
            with open("registry.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
            plugins = data.get("plugins_disponibles", [])
            if not plugins:
                lbl = ctk.CTkLabel(frame_plugins, text="No hay plugins en el registro.", text_color="#a0a0a0")
                lbl.pack(padx=5, pady=5)
                return
                
            for p in plugins:
                nombre = p["nombre"]
                desc = p["descripcion"]
                
                # Fila para cada plugin
                fila = ctk.CTkFrame(frame_plugins, fg_color="#18151f")
                fila.pack(fill="x", padx=5, pady=5, ipadx=5, ipady=5)
                
                lbl_info = ctk.CTkLabel(fila, text=f"📌 {nombre}\n{desc}", font=ctk.CTkFont(size=10), justify="left", text_color="#e0e0e0")
                lbl_info.pack(side="left", padx=5, anchor="w")
                
                btn_inst = ctk.CTkButton(
                    fila, 
                    text="📥 Instalar", 
                    width=90, 
                    height=28,
                    fg_color="#990000", 
                    hover_color="#ff0033",
                    command=lambda n=nombre: instalar_plugin(n)
                )
                btn_inst.pack(side="right", padx=5)
        else:
            lbl = ctk.CTkLabel(frame_plugins, text="Error: Falta el archivo registry.json", text_color="#ff4444")
            lbl.pack(padx=5, pady=5)
    except Exception as e:
        lbl = ctk.CTkLabel(frame_plugins, text=f"Error leyendo registro: {e}", text_color="#ff4444")
        lbl.pack(padx=5, pady=5)

def instalar_plugin(nombre_plugin):
    try:
        lbl_estado_gp.configure(text=f"● Descargando {nombre_plugin} desde GitHub...", text_color="orange")
        
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
            
        # Descarga mediante urllib
        urllib.request.urlretrieve(url_a_descargar, archivo_destino)
        
        lbl_estado_gp.configure(text=f"● ¡{nombre_plugin} instalado! Reinicia la app.", text_color="#00ff66")
        
    except urllib.error.HTTPError as e:
        lbl_estado_gp.configure(text=f"● Error HTTP {e.code}: Sube el archivo a GitHub.", text_color="red")
    except Exception as e:
        lbl_estado_gp.configure(text=f"● Error al instalar: {e}", text_color="red")