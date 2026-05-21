import tkinter as tk

class MenuBienvenidaFrame(tk.Frame):
    """
    Esta clase es un Frame especializado que representa el menú principal.
    Al heredar de tk.Frame, este objeto adquiere todas las propiedades de un contenedor.
    """
    def __init__(self, master):
        # super().__init__(master) inicializa el Frame dentro de la ventana principal ('master').
        # Definimos un color de fondo gris claro (#f0f2f5).
        super().__init__(master, bg="#f0f2f5")
        
        # 'self.master' guarda la referencia a la ventana principal (main.py)
        # Esto nos permite invocar su método 'mostrar_pantalla()' para navegar.
        self.master = master
        
        # Título
        titulo = tk.Label(
            self, 
            text="Bienvenido al Sistema de Gestión", 
            font=("Arial", 24, "bold"), 
            bg="#f0f2f5", 
            fg="#333333"
        )
        # .pack() posiciona los elementos de forma vertical y secuencial dentro de ESTE Frame.
        titulo.pack(pady=60)
        
        # Creamos un sub-frame interno únicamente para agrupar y centrar los botones principales.
        frame_botones = tk.Frame(self, bg="#f0f2f5")
        frame_botones.pack(expand=True)

        # Botón para ir a Inventario
        btn_inventario = tk.Button(
            frame_botones,
            text="Gestionar Inventario",
            font=("Arial", 14, "bold"),
            bg="#10b981", fg="white",
            width=22, height=3, cursor="hand2",
            # El parámetro command ejecuta una función anónima (lambda) que le avisa
            # a la ventana principal que debe destruir este frame y montar el de Inventario.
            command=lambda: self.importar_y_navegar("InventoryFrame")
        )
        # Dentro de 'frame_botones' usamos .grid() para poner los botones lado a lado (columna 0 y 1).
        btn_inventario.grid(row=0, column=0, padx=20, pady=10)

        # Botón para ir a Ventas
        btn_venta = tk.Button(
            frame_botones,
            text="Nueva Venta",
            font=("Arial", 14, "bold"),
            bg="#3b82f6", fg="white",
            width=22, height=3, cursor="hand2",
            command=lambda: self.importar_y_navegar("SalesFrame")
        )
        btn_venta.grid(row=0, column=1, padx=20, pady=10)

    def importar_y_navegar(self, nombre_pantalla):
        """Evita las importaciones circulares importando las pantallas bajo demanda al hacer clic."""
        if nombre_pantalla == "InventoryFrame":
            from ui.inventario import InventoryFrame
            self.master.mostrar_pantalla(InventoryFrame)
        elif nombre_pantalla == "SalesFrame":
            from ui.ventas import SalesFrame
            self.master.mostrar_pantalla(SalesFrame)