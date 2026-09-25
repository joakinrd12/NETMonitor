import os
import importlib
import customtkinter as ctk

class NetMonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("NetMonitor Dashboard (Open Source)")
        self.geometry("900x600")
        
        # Configurar tema visual general
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        # Título principal del Dashboard
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=20, pady=15)
        
        self.logo_label = ctk.CTkLabel(
            self.header_frame, 
            text="⚡ NetMonitor Dashboard", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.logo_label.pack(side="left")
        
        # Contenedor principal con Scroll para las tarjetas
        self.dashboard_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.dashboard_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configurar diseño de columnas para las tarjetas (2 columnas)
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        self.dashboard_frame.grid_columnconfigure(1, weight=1)
        
        self.fila_actual = 0
        self.columna_actual = 0
        
        # Cargar plugins automáticamente como tarjetas
        self.cargar_plugins()

    def cargar_plugins(self):
        plugins_dir = "plugins"
        if not os.path.exists(plugins_dir):
            os.makedirs(plugins_dir)
            
        for archivo in os.listdir(plugins_dir):
            if archivo.endswith(".py") and archivo != "__init__.py":
                nombre_modulo = archivo[:-3]
                try:
                    modulo = importlib.import_module(f"plugins.{nombre_modulo}")
                    # Cada plugin ahora proveerá una tarjeta para el dashboard
                    if hasattr(modulo, "crear_tarjeta"):
                        modulo.crear_tarjeta(self)
                except Exception as e:
                    print(f"Error al cargar el plugin {nombre_modulo}: {e}")

    def agregar_tarjeta_dashboard(self, titulo):
        """Crea una tarjeta contenedora estilizada y devuelve su cuerpo para que el plugin dibuje dentro"""
        card = ctk.CTkFrame(self.dashboard_frame, corner_radius=10)
        card.grid(row=self.fila_actual, column=self.columna_actual, sticky="nsew", padx=10, pady=10)
        
        # Título de la tarjeta
        lbl_titulo = ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=14, weight="bold"))
        lbl_titulo.pack(anchor="w", padx=15, pady=(10, 5))
        
        # Administrar posición en la grilla (2 columnas)
        self.columna_actual += 1
        if self.columna_actual > 1:
            self.columna_actual = 0
            self.fila_actual += 1
            
        return card