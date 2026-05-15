# Módulo 1 — Ciclo de Vida y Widgets en Tkinter

## ¿Qué es el ciclo de vida de una aplicación Tkinter?

El ciclo de vida representa el flujo completo de una aplicación gráfica desde que se crea hasta que se cierra.

### Etapas principales

|Etapa|Explicación|
|---|---|
|`Tk()`|Crea la ventana principal y arranca el motor gráfico Tcl/Tk|
|Configuración|Se agregan widgets, títulos, tamaños y propiedades|
|`mainloop()`|Mantiene viva la aplicación escuchando eventos|

---

# Funciones y métodos utilizados

## `tk.Tk()`

### ¿Qué hace?

Inicializa la aplicación gráfica y crea la ventana principal.

### Sintaxis

```
root = tk.Tk()
```

### Uso real

Toda aplicación de escritorio necesita una ventana raíz:

- sistemas administrativos,
- inventarios,
- dashboards,
- POS de ventas,
- formularios.

---

## `.title()`

### ¿Qué hace?

Define el título de la ventana.

### Sintaxis

```
root.title("Mi aplicación")
```

### Parámetros

|Parámetro|Explicación|
|---|---|
|texto|Nombre mostrado en la barra superior|

### Uso real

Identificar módulos:

- “Sistema de Ventas”
- “Gestión Académica”
- “Inventario”

---

## `.geometry()`

### ¿Qué hace?

Define tamaño inicial de la ventana.

### Sintaxis

```
root.geometry("300x200")
```

### Parámetros

|Parámetro|Explicación|
|---|---|
|`"ancho x alto"`|Tamaño en píxeles|

### Uso real

Controlar resolución de:

- kioscos,
- paneles administrativos,
- software industrial.

---

# Widgets básicos

## `Label`

### ¿Qué hace?

Muestra texto informativo.

### Sintaxis

```
tk.Label(master, text="Hola")
```

### Parámetros importantes

|Parámetro|Función|
|---|---|
|`master`|Contenedor padre|
|`text`|Texto visible|
|`font`|Fuente|
|`bg`|Fondo|
|`fg`|Color del texto|

### Uso real

- nombres de campos,
- títulos,
- estados del sistema.

---

## `Entry`

### ¿Qué hace?

Permite ingresar texto.

### Sintaxis

```
tk.Entry(master)
```

### Métodos importantes

## `.get()`

### ¿Qué hace?

Obtiene el texto escrito.

```
valor = entry.get()
```

### Uso real

Capturar:

- usuarios,
- contraseñas,
- correos,
- códigos.

---

## `Button`

### ¿Qué hace?

Ejecuta acciones.

### Sintaxis

```
tk.Button(master, text="Guardar", command=funcion)
```

### Parámetros importantes

|Parámetro|Función|
|---|---|
|`text`|Texto del botón|
|`command`|Función a ejecutar|
|`bg`|Color de fondo|
|`fg`|Color del texto|

### Uso real

- guardar,
- eliminar,
- iniciar sesión,
- exportar PDF.

---

# Métodos de geometría

## `.pack()`

### ¿Qué hace?

Organiza widgets automáticamente.

### Sintaxis

```
widget.pack()
```

### Parámetros importantes

|Parámetro|Función|
|---|---|
|`pady`|Espacio vertical|
|`padx`|Espacio horizontal|
|`side`|Posición|

### Uso real

Interfaces rápidas y pequeñas.

---

# Ejemplo completo

```python
import tkinter as tk
class Aplicacion:    
    def __init__(self, root):        
        self.root = root        
        self.root.title("Saludo")        
        self.root.geometry("300x200")        
        self.label = tk.Label(root, text="Introduce tu nombre:")        
        self.label.pack(pady=10)        
        self.entry = tk.Entry(root)        
        self.entry.pack(pady=5)        
        self.boton = tk.Button(root, text="Saludar" command=self.saludar)        
        self.boton.pack(pady=10)    
    def saludar(self):        
        nombre = self.entry.get()        
        print(f"Hola {nombre}")
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
```

---

# Ejercicios — Módulo 1

## Ejercicio 1

Crear una ventana que:

- solicite nombre y edad,
- tenga un botón “Mostrar”,
- imprima los datos en consola.

---

## Ejercicio 2

Crear una mini calculadora que:

- tenga dos `Entry`,
- un botón “Sumar”,
- muestre el resultado en un `Label`.