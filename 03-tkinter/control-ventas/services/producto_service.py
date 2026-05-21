from db.conexion import insertar_producto

def registrar_nuevo_producto(nombre, precio_raw, stock_raw, categoria):
    """
    Procesa y valida los datos provenientes del formulario de la UI.
    Devuelve un diccionario indicando si la operación fue exitosa o si hubo un error.
    """
    # 1. Limpiar espacios en blanco innecesarios
    nombre = nombre.strip()
    categoria = categoria.strip()
    
    # 2. Validación: Ningún campo debe quedar vacío
    if not (nombre and precio_raw and stock_raw and categoria):
        return {"exito": False, "tipo_error": "campos_vacios", "mensaje": "Todos los campos son obligatorios."}
    
    # 3. Validación: Comprobar formatos numéricos correctos
    try:
        precio = float(precio_raw)
        if precio < 0:
            return {"exito": False, "tipo_error": "valor_negativo", "mensaje": "El precio no puede ser negativo."}
            
        stock = int(stock_raw)
        if stock < 0:
            return {"exito": False, "tipo_error": "valor_negativo", "mensaje": "El stock no puede ser negativo."}
            
    except ValueError:
        return {"exito": False, "tipo_error": "formato_invalido", "mensaje": "El precio debe ser un número decimal y el stock un entero."}
    
    # 4. Si todo está correcto, delegamos el almacenamiento a la capa DB
    try:
        insertar_producto(nombre, precio, stock, categoria)
        return {"exito": True, "mensaje": f"Producto '{nombre}' guardado con éxito."}
    except Exception as e:
        return {"exito": False, "tipo_error": "db_error", "mensaje": f"Error crítico en la base de datos: {e}"}