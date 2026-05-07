# Análisis de Contenido Streaming

## Archivo para generar csv

```python
import pandas as pd
import numpy as np

# Creamos datos de ejemplo para la clase
data = {
    'titulo': ['The Witcher', 'Stranger Things', 'Dark', 'The Crown', 'Dark', 'Office', 'Inception', 'Batman', None, 'Interstellar'],
    'tipo': ['Serie', 'Serie', 'Serie', 'Serie', 'Serie', 'Serie', 'Película', 'Película', 'Película', 'Película'],
    'vistas_millones': [120.5, 150.2, 89.0, 75.4, 89.0, 200.1, 305.7, 250.0, 100.0, 180.5],
    'puntuacion': [8.2, 9.1, 9.5, 8.8, 9.5, 9.0, 8.8, 9.2, 7.5, np.nan],
    'año_lanzamiento': [2019, 2016, 2017, 2016, 2017, 2005, 2010, 2022, 2021, 2014]
}

df = pd.DataFrame(data)
df.to_csv('streaming_data.csv', index=False)
print("Archivo 'streaming_data.csv' generado con éxito.")
```

## Requerimientos 

### 1. Carga e Identificación de Duplicados
A veces, por errores de sistema, los datos se repiten.
- **Función**: df.duplicated() nos dice si hay filas idénticas.
- **Función**: df.drop_duplicates() las elimina.
- **Reto**: Elimina los duplicados del archivo y guarda el resultado en el mismo df.

### 2. Limpieza de "Vacíos" (NaN)
Un dato vacío puede arruinar un promedio.
- **Función**: df.fillna(valor) reemplaza los nulos con algo específico.
- **Reto**: En la columna puntuacion, reemplaza los valores nulos con un 0.

### 3. El Método .loc[] (Filtrado Inteligente)
A diferencia de los filtros básicos, .loc es la forma profesional de acceder a grupos de filas y columnas.
- **Sintaxis**: df.loc[filas, columnas]
- **Reto**: Crea un nuevo DataFrame llamado exitos que contenga solo las filas donde vistas_millones sea mayor a 150 y solo las columnas titulo y vistas_millones.

### 4. Estadísticas Rápidas
- **Función**: df['columna'].describe() te da un resumen completo (mínimo, máximo, media).
- **Reto**: Obtén el resumen estadístico de la columna vistas_millones.

## Cierre

1. Calculer una nueva columna llamada "Puntuación Total", que sea la multiplicación de vistas_millones por puntuacion. 
2. Ordenar el DataFrame por esa nueva columna de mayor a menor.
