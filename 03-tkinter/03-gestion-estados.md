# Módulo 3 — Gestión de Estados y Treeview

# Gestión de Estados

## ¿Qué es?

Permite controlar:

- cuándo un widget está activo,
- cuándo se bloquea,
- cuándo cambia automáticamente.

---

# Variables de control

## `StringVar()`

### ¿Qué hace?

Guarda texto dinámicamente.

### Sintaxis

```
variable = tk.StringVar()
```

---

# Métodos importantes

## `.set()`

### ¿Qué hace?

Cambia el valor.

```
variable.set("Hola")
```

---

## `.get()`

### ¿Qué hace?

Obtiene el valor actual.

```
valor = variable.get()
```

---

## `.trace_add()`

### ¿Qué hace?

Ejecuta una función automáticamente cuando cambia la variable.

### Sintaxis

```
variable.trace_add("write", funcion)
```

### Parámetros

|Parámetro|Función|
|---|---|
|`"write"`|Detecta escritura|
|callback|Función a ejecutar|

### Uso real

- validaciones,
- formularios dinámicos,
- activación automática de botones.

---

# Parámetro `state`

## Estados disponibles

|Estado|Función|
|---|---|
|`"normal"`|Activo|
|`"disabled"`|Bloqueado|
|`"readonly"`|Solo lectura|

---

# Treeview

## ¿Qué es?

Widget avanzado de tablas perteneciente a `ttk`.

### Importación

```
from tkinter import ttk
```

---

# Métodos importantes del Treeview

## `Treeview()`

### Sintaxis

```
ttk.Treeview(    master,    columns=("id", "nombre"),    show="headings")
```

### Parámetros

|Parámetro|Función|
|---|---|
|`columns`|Columnas|
|`show`|Mostrar encabezados|
|`selectmode`|Tipo de selección|

---

## `.heading()`

### ¿Qué hace?

Define nombres visibles de columnas.

```
tabla.heading("id", text="ID")
```

---

## `.column()`

### ¿Qué hace?

Configura ancho y alineación.

```
tabla.column("id", width=100)
```

---

## `.insert()`

### ¿Qué hace?

Inserta filas.

```
tabla.insert("", "end", values=("1", "Jesús"))
```

### Parámetros

|Parámetro|Función|
|---|---|
|`parent`|Padre|
|`index`|Posición|
|`values`|Datos|

---

## `.selection()`

### ¿Qué hace?

Obtiene fila seleccionada.

```
seleccion = tabla.selection()
```

---

## `.delete()`

### ¿Qué hace?

Elimina filas.

```
tabla.delete(item_id)
```

---

# Ejemplo completo

```python
import tkinter as tk  
from tkinter import ttk  
  
root = tk.Tk()  
  
tabla = ttk.Treeview(  
root,  
columns=("id", "nombre"),  
show="headings"  
)  
  
tabla.heading("id", text="ID")  
tabla.heading("nombre", text="Nombre")  
  
tabla.pack()  
  
tabla.insert("", "end", values=("1", "Astrid"))  
tabla.insert("", "end", values=("2", "Jesús"))  
  
root.mainloop()
```

---

# Ejercicios — Módulo 3

## Ejercicio 1

Crear un sistema donde:

- el botón “Enviar” inicie deshabilitado,
- se habilite automáticamente cuando el usuario escriba más de 5 caracteres.

---

## Ejercicio 2

Crear una tabla `Treeview` que:

- permita agregar estudiantes,
- permita eliminar estudiantes seleccionados,
- tenga columnas:
    - ID,
    - Nombre,
    - Carrera.