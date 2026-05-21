import tkinter as tk
from tkinter import messagebox
from services.producto_service import registrar_nuevo_producto

class InventoryFrame(tk.Frame):
    """Frame que contiene el formulario alineado con .grid() para el alta de productos."""
    def __init__(self, master):
        # Inicializamos el contenedor con fondo blanco
        super().__init__(master, bg="#ffffff")
        self.master = master
        
        titulo = tk.Label(self, text="Alta de Productos (Inventario)", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e293b")
        titulo.pack(pady=30)
        
        # --- EL SISTEMA DE REJILLA (.grid()) ---
        # Construimos un contenedor intermedio donde organizaremos las etiquetas y cajas de texto.
        formulario = tk.Frame(self, bg="#ffffff")
        formulario.pack(pady=20)
        
        lbl_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        
        # Fila 0: Nombre
        # sticky="w" (West/Oeste) obliga al texto a alinearse a la izquierda de su celda.
        tk.Label(formulario, text="Nombre del Producto:", font=lbl_font, bg="#ffffff").grid(row=0, column=0, sticky="w", padx=15, pady=12)
        self.entry_nombre = tk.Entry(formulario, font=entry_font, width=30, bd=2, relief="groove")
        # sticky="e" (East/Este) obliga a la caja de texto a pegarse al borde derecho de su celda.
        self.entry_nombre.grid(row=0, column=1, sticky="e", padx=15, pady=12)
        
        # Fila 1: Precio
        tk.Label(formulario, text="Precio ($):", font=lbl_font, bg="#ffffff").grid(row=1, column=0, sticky="w", padx=15, pady=12)
        self.entry_precio = tk.Entry(formulario, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_precio.grid(row=1, column=1, sticky="e", padx=15, pady=12)
        
        # Fila 2: Stock
        tk.Label(formulario, text="Stock Inicial:", font=lbl_font, bg="#ffffff").grid(row=2, column=0, sticky="w", padx=15, pady=12)
        self.entry_stock = tk.Entry(formulario, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_stock.grid(row=2, column=1, sticky="e", padx=15, pady=12)
        
        # Fila 3: Categoría
        tk.Label(formulario, text="Categoría:", font=lbl_font, bg="#ffffff").grid(row=3, column=0, sticky="w", padx=15, pady=12)
        self.entry_categoria = tk.Entry(formulario, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_categoria.grid(row=3, column=1, sticky="e", padx=15, pady=12)
        
        # --- PANEL DE ACCIONES ---
        frame_acciones = tk.Frame(self, bg="#ffffff")
        frame_acciones.pack(pady=40)
        
        btn_guardar = tk.Button(frame_acciones, text="Guardar en BD", font=("Arial", 11, "bold"), bg="#10b981", fg="white", width=15, command=self.ejecutar_guardado)
        btn_guardar.grid(row=0, column=0, padx=10)
        
        # Para regresar al menú, importamos de forma local para evitar bucles infinitos de importación.
        from ui.menu_bienvenida import MenuBienvenidaFrame
        btn_volver = tk.Button(frame_acciones, text="Volver al Menú", font=("Arial", 11), bg="#64748b", fg="white", width=15, command=lambda: master.mostrar_pantalla(MenuBienvenidaFrame))
        btn_volver.grid(row=0, column=1, padx=10)

    def ejecutar_guardado(self):
        """Extrae el texto de la interfaz gráfica y lo envía a la capa de servicios."""
        # Obtenemos los strings crudos usando .get()
        res = registrar_nuevo_producto(
            self.entry_nombre.get(),
            self.entry_precio.get(),
            self.entry_stock.get(),
            self.entry_categoria.get()
        )
        
        # Según lo que responda el servicio, mostramos una alerta gráfica adecuada
        if res["exito"]:
            messagebox.showinfo("Éxito", res["mensaje"])
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", res["mensaje"])

    def limpiar_formulario(self):
        """Borra el contenido visual de todas las cajas de texto."""
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)