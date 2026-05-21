import tkinter as tk
from tkinter import ttk, messagebox

class SalesFrame(tk.Frame):
    """Frame que gestiona la visualización interactiva del carrito mediante un Treeview."""
    def __init__(self, master):
        super().__init__(master, bg="#ffffff")
        self.master = master
        
        titulo = tk.Label(self, text="Carrito de Compras Actual", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e293b")
        titulo.pack(pady=25)
        
        # Contenedor para agrupar la tabla y su barra de desplazamiento vertical (Scrollbar)
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(pady=10)
        
        # Definición estructural de las columnas
        columnas = ("id", "producto", "precio", "cantidad", "total")
        # show="headings" oculta una columna en blanco por defecto que Tkinter añade a la izquierda.
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
        
        # Textos de cabecera que verá el usuario
        self.tabla.heading("id", text="ID Ítem")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("precio", text="Precio Unitario")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.heading("total", text="Total")
        
        # Ancho y alineaciones internas (c=center, w=west/izquierda, e=east/derecha)
        self.tabla.column("id", width=80, anchor="center")
        self.tabla.column("producto", width=250, anchor="w")
        self.tabla.column("precio", width=120, anchor="e")
        self.tabla.column("cantidad", width=100, anchor="center")
        self.tabla.column("total", width=120, anchor="e")
        
        # Añadimos la barra de scroll y la vinculamos al movimiento vertical de la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        # Colocamos la tabla a la izquierda y el scroll a la derecha rellenando el eje Y
        self.tabla.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        
        self.cargar_datos_demo()
        
        # --- CONTROLES INFERIORES ---
        frame_controles = tk.Frame(self, bg="#ffffff")
        frame_controles.pack(pady=30)
        
        btn_eliminar = tk.Button(frame_controles, text="Eliminar Seleccionado", font=("Arial", 11, "bold"), bg="#ef4444", fg="white", width=20, command=self.eliminar_fila)
        btn_eliminar.grid(row=0, column=0, padx=15)
        
        from ui.menu_bienvenida import MenuBienvenidaFrame
        btn_volver = tk.Button(frame_controles, text="Volver al Menú", font=("Arial", 11), bg="#64748b", fg="white", width=15, command=lambda: master.mostrar_pantalla(MenuBienvenidaFrame))
        btn_volver.grid(row=0, column=1, padx=15)

    def cargar_datos_demo(self):
        """Puebla de forma ficticia el Treeview para probar su dinamismo."""
        items = [
            ("1", "Laptop HP ProBook", "$ 750.00", "1", "$ 750.00"),
            ("2", "Mouse Óptico Inalámbrico", "$ 25.00", "2", "$ 50.00"),
            ("3", "Monitor Gamer 24' Dell", "$ 180.00", "1", "$ 180.00")
        ]
        for item in items:
            self.tabla.insert("", tk.END, values=item)

    def eliminar_fila(self):
        """Captura los IDs internos del Treeview seleccionados por el usuario y los borra."""
        # .selection() nos devuelve una tupla con los identificadores de las filas seleccionadas
        seleccion = self.tabla.selection()
        
        if not seleccion:
            messagebox.showwarning("Sin selección", "Por favor, selecciona un elemento de la tabla para eliminarlo.")
            return
            
        # Recorremos la selección y eliminamos la fila del componente visual
        for item_id in seleccion:
            self.tabla.delete(item_id)
            
        messagebox.showinfo("Carrito actualizado", "El ítem seleccionado ha sido removido.")