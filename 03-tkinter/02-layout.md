# Módulo 2 — Layout con `grid()` y `Frame`

## ¿Qué es un Layout?

El layout es la organización visual de los widgets.

Tkinter ofrece varios sistemas:

- `pack()`
- `grid()`
- `place()`

El más profesional es `grid()`.

---

# El widget `Frame`

## ¿Qué hace?

Un `Frame` es un contenedor para organizar otros widgets.

### Sintaxis

```
frame = tk.Frame(root)
```

### Parámetros importantes

|Parámetro|Función|
|---|---|
|`padx`|Espaciado horizontal|
|`pady`|Espaciado vertical|
|`bg`|Fondo|

### Uso real

Separar secciones:

- menús,
- formularios,
- paneles,
- dashboards.

---

# `.grid()`

## ¿Qué hace?

Organiza widgets usando filas y columnas.

### Sintaxis

```
widget.grid(row=0, column=0)
```

---

# Parámetros importantes de `grid`

|Parámetro|Función|
|---|---|
|`row`|Fila|
|`column`|Columna|
|`padx`|Espacio horizontal|
|`pady`|Espacio vertical|
|`sticky`|Alineación|
|`columnspan`|Unir columnas|
|`rowspan`|Unir filas|

---

# `sticky`

## ¿Qué hace?

Define hacia dónde se estira o alinea el widget.

### Valores

|Valor|Dirección|
|---|---|
|`"n"`|Arriba|
|`"s"`|Abajo|
|`"e"`|Derecha|
|`"w"`|Izquierda|
|`"nsew"`|Expandir completo|

---

# `.columnconfigure()`

## ¿Qué hace?

Permite que las columnas crezcan dinámicamente.

### Sintaxis

```
root.columnconfigure(0, weight=1)
```

### Parámetros

|Parámetro|Función|
|---|---|
|índice|columna|
|`weight`|prioridad de expansión|

### Uso real

Crear interfaces responsivas.

---

# Ejemplo completo

```python
import tkinter as tk  
  
root = tk.Tk()  
root.title("Formulario")  
  
frame = tk.Frame(root, padx=20, pady=20)  
frame.pack()  
  
tk.Label(frame, text="Nombre").grid(  
row=0,  
column=0,  
sticky="w"  
)  
  
entry_nombre = tk.Entry(frame)  
entry_nombre.grid(  
row=0,  
column=1,  
padx=10  
)  
  
tk.Label(frame, text="Correo").grid(  
row=1,  
column=0,  
sticky="w"  
)  
  
entry_correo = tk.Entry(frame)  
entry_correo.grid(  
row=1,  
column=1,  
padx=10  
)  
  
btn = tk.Button(frame, text="Guardar")  
btn.grid(  
row=2,  
column=1,  
pady=10,  
sticky="e"  
)  
  
root.mainloop()
```

---

# Ejercicios — Módulo 2

## Ejercicio 1

Crear un formulario de registro con:

- nombre,
- apellido,
- teléfono,
- botón guardar.

Todo usando `grid()`.

---

## Ejercicio 2

Crear una interfaz tipo login:

- usuario,
- contraseña,
- botón iniciar sesión,
- usando `Frame` y `grid()`.