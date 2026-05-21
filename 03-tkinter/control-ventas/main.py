import tkinter as tk
from db.conexion import inicializar_db
from ui.menu_bienvenida import MenuBienvenidaFrame

class SistemaVentasApp(tk.Tk):
    """
    Clase principal que hereda de tk.Tk (la ventana base del sistema operativo).
    Funciona como el controlador central o enrutador de nuestra aplicación.
    """
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ventas e Inventario")
        
        # Centrar y dimensionar la ventana principal (800x600)
        self.centrar_ventana(800, 600)
        
        # Ejecutamos la inicialización de la base de datos (Fase 5) al arrancar
        inicializar_db()
        
        # Esta variable guardará el Frame (pantalla) que se está mostrando actualmente.
        self.frame_actual = None
        
        # Arrancamos cargando la pantalla del menú de bienvenida de forma predeterminada
        self.mostrar_pantalla(MenuBienvenidaFrame)

    def centrar_ventana(self, ancho, alto):
        """Calcula las proporciones del monitor del usuario para colocar la app en el centro."""
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        
        pos_x = int((pantalla_ancho / 2) - (ancho / 2))
        pos_y = int((pantalla_alto / 2) - (alto / 2))
        
        # Estructura del string de geometría: "ANCHO x ALTO + POS_X + POS_Y"
        self.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
        self.resizable(False, False) # Bloqueamos el rediseño manual para evitar deformaciones

    def mostrar_pantalla(self, clase_frame):
        """
        CICLO DE VIDA DEL FRAME:
        Este método recibe una Clase de Frame, destruye la pantalla que estaba abierta anteriormente
        para liberar la memoria RAM y monta el nuevo lienzo de forma limpia.
        """
        # 1. Si ya hay una pantalla dibujada, la eliminamos por completo del mapa
        if self.frame_actual is not None:
            self.frame_actual.destroy()
            
        # 2. Instanciamos la nueva clase de pantalla.
        # Le pasamos 'self' (la ventana principal) como argumento para que el frame sepa quién es su padre.
        self.frame_actual = clase_frame(self)
        
        # 3. Hacemos que el nuevo Frame ocupe la totalidad del tamaño disponible de la ventana
        self.frame_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    # Instanciamos la ventana raíz
    app = SistemaVentasApp()
    # Encendemos el bucle infinito de eventos de Tkinter (espera clics, pulsaciones de teclas, etc.)
    app.mainloop()