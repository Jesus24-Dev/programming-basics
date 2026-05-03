# Personal Expense Tracker (CLI)

El objetivo es construir un script que lea un archivo de texto con transacciones "crudas", las limpie, las clasifique y genere un reporte de ahorros.

## 1. El Origen de los Datos

Crea un archivo llamado `gastos.csv` con el siguiente formato (incluyendo algunos errores a propósito para practicar el manejo de excepciones):

```Plaintext
fecha,descripcion,categoria,monto
2026-05-01,Supermercado,Comida,50.25
2026-05-02,Suscripción Streaming,Entretenimiento,15.00
2026-05-02,Cena restaurante,Comida,error_dato
2026-05-03,Gasolina,Transporte,40.00
2026-05-04,Libro Python,Educación,25.50
```

## 2. Requerimientos Técnicos

Para completar este bloque, tu código debe cumplir con lo siguiente:

- **Lectura Manual:** Usa `open()` y el método `.readlines()` o el módulo nativo `csv`. No uses herramientas automáticas; procesa cada línea como un **string**.
    
- **Limpieza de Datos:** Implementa una función que convierta los strings de monto en **floats**. Usa un bloque `try/except` para saltar las líneas que tengan errores (como el "error_dato" del ejemplo) y notificar al usuario.
    
- **Estructuras de Datos:**
    
    - Almacena cada transacción en un **diccionario**.
        
    - Guarda todos los diccionarios dentro de una **lista** principal.
        
- **Transformación y Filtro:** Crea funciones para:
    
    - Calcular el gasto total.
        
    - Agrupar gastos por categoría (usando un diccionario donde las llaves sean las categorías).
        
    - Filtrar gastos mayores a un monto específico definido por el usuario.
        

## 3. Flujo de Ejecución Sugerido

1. **Carga:** Leer el archivo línea por línea.
    
2. **Procesamiento:** Separar los valores por comas (`.split(',')`).
    
3. **Validación:** Verificar que el monto sea numérico antes de sumarlo.
    
4. **Análisis:** Iterar sobre la lista de diccionarios para sumar los montos por cada categoría.
    
5. **Salida:** Imprimir un resumen en consola con un formato limpio.

## Formas de leer un csv

### 1. Forma manual con Python puro

```python
with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    
    # La primera línea suele ser el encabezado
    encabezado = lineas[0].strip().split(',')
    
    for linea in lineas[1:]:
        # Limpiamos saltos de línea y separamos por comas
        datos = linea.strip().split(',')
        print(f"Procesando: {datos}")
```

### 2. Usando el modulo nativo `csv`
```python
import csv

with open('datos.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        # Cada 'fila' es una lista de strings
        print(fila)
```
