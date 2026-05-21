import sqlite3

DATABASE_NAME = "ventas.db"

def inicializar_db():
    """Crea la tabla de productos si no existe al arrancar la app."""
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def insertar_producto(nombre, precio, stock, categoria):
    """Inserta un registro de forma segura usando tuplas para evitar SQL Injection."""
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (?, ?, ?, ?)",
        (nombre, precio, stock, categoria)
    )
    conexion.commit()
    conexion.close()