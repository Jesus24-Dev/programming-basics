# Conceptos basicos 

## ¿Qué es Pandas?
Pandas es una librería de código abierto para Python especializada en la manipulación y análisis de datos. Su nombre proviene de "Panel Data" (un término técnico para datos estructurados).

A diferencia de las hojas de cálculo tradicionales, Pandas te permite manejar millones de datos de forma automática, rápida y reproducible mediante código.

## Los 3 Pilares: Series, DataFrame e Índice
Para entender Pandas, imagina un libro de Excel, pero con "superpoderes":

- **Series**: Es el objeto más básico de Pandas. Imagínalo como una única columna de datos (por ejemplo, solo la lista de nombres de los productos). Tiene una sola dimensión.

- **DataFrame**: Es la estructura principal. Es una tabla bidimensional (filas y columnas), muy parecida a una hoja de cálculo. Un DataFrame es, esencialmente, un conjunto de Series pegadas una al lado de la otra.

- **Índice (Index)**: Es la "etiqueta" de cada fila. Por defecto, Pandas numera las filas del 0 en adelante. El índice es lo que permite a Pandas encontrar un dato específico de forma instantánea.

## ¿Qué es un archivo CSV?
CSV significa Comma Separated Values (Valores Separados por Comas). Es el formato de archivo más común en la ciencia de datos porque:

- Es un archivo de texto simple (puedes abrirlo con el Bloc de Notas).
- Cada línea es una fila y cada coma separa una columna.
- Ventaja: No pesa casi nada y es universal (cualquier software lo entiende).

## Conceptos Operativos Clave
Estos son términos que leerás constantemente en tutoriales y documentación:

| Concepto | Definición Simple |
| :--- | :--- | 
| Parsing | El proceso de leer un archivo (como un CSV) y convertirlo en un DataFrame que Python pueda entender. |
| NaN (Not a Number) | Es la forma en que Pandas marca un dato faltante o un espacio vacío en tu tabla.|
| Vectorización | Es la capacidad de Pandas de aplicar una operación (como una suma) a toda una columna a la vez, sin usar bucles for. Es lo que hace que Pandas sea ultra rápido. |
| Casting | Cambiar el tipo de dato de una columna (ejemplo: pasar una columna de "texto" a "números enteros"). |
| Broadcasting | Cuando aplicas una operación de una sola cifra a toda una columna (ejemplo: df['precio'] * 1.15 para aplicar el 15% de impuesto a todos). |

## El flujo de trabajo estándar (Data Pipeline)
Cuando trabajas con Pandas, casi siempre sigues este orden lógico:

- **Ingesta**: Importar los datos (read_csv, read_excel).
- **Exploración**: Ver qué hay dentro (head, info, describe).
- **Limpieza**: Arreglar nulos (dropna, fillna) y corregir nombres de columnas.
- **Transformación**: Crear nuevas columnas o filtrar datos.
- **Agregación**: Resumir los datos (groupby, sum, mean).
- **Salida**: Guardar el resultado limpio en un nuevo archivo (to_csv).

##  Diccionario de Funciones Esenciales
### Fase A: Ingesta y Exploración
- `pd.read_csv()`: Abre archivos CSV y los convierte en DataFrames.
- `df.head(n)`: Muestra las primeras n filas (por defecto 5). Ideal para un vistazo rápido.
- `df.info()`: Muestra un resumen técnico: nombres de columnas, cuántos datos no son nulos y el tipo de dato (entero, flotante, objeto).
- `df.describe()`: Genera estadísticas automáticas (media, máximo, mínimo, etc.) de las columnas numéricas.

### Fase B: Limpieza (Data Cleaning)
- `df.rename()`: Cambia el nombre de columnas o índices.
- `df.dropna()`: Elimina filas o columnas que contienen valores vacíos (NaN).
- `df.fillna(valor)`: Rellena los espacios vacíos con un valor específico (como un 0 o la palabra "Desconocido").
- `df.drop_duplicates()`: Busca y elimina filas que estén repetidas exactamente igual.
- `df['col'].astype()`: Cambia el tipo de dato de una columna (ej. de texto a número).

### Fase C: Selección y Filtro
- `df['columna']`: Selecciona una sola columna (Series).
- `df[['col1', 'col2']]`: Selecciona varias columnas a la vez.
- `df.loc[]`: Filtra por etiquetas o condiciones lógicas (ej. df.loc[df['precio'] > 100]).
- `df.iloc[]`: Filtra por posición numérica (ej. "dame la fila 0 y la columna 1").

### Fase D: Transformación y Cálculo
- `df.sort_values()`: Ordena la tabla según una columna (ascendente o descendente).
- `df['col'].value_counts()`: Cuenta cuántas veces aparece cada valor único en una columna. Muy útil para saber cuál es el "producto más vendido".
- `df.groupby()`: Agrupa los datos en categorías para realizar cálculos por grupo (ej. suma de ventas por país).
- `df.apply()`: Permite aplicar una función personalizada a cada fila o columna.

## Lista de Operaciones Matemáticas Rápidas
Estas se aplican directamente sobre una columna o sobre todo el DataFrame:

- `.sum()`: Suma total.
- `.mean()`: Promedio aritmético.
- `.median()`: El valor central de los datos.
- `.max() / .min()`: Valores extremos.
- `.count()`: Cuenta cuántos valores hay (ignorando los vacíos).

## Uso combinado de funciones 
```python
import pandas as pd

# 1. Leer
df = pd.read_csv('datos.csv')

# 2. Limpiar nombres y nulos
df.columns = df.columns.str.lower()
df = df.dropna()

# 3. Transformar (Crear columna)
df['total'] = df['cantidad'] * df['precio']

# 4. Analizar (Agrupar)
reporte = df.groupby('categoria')['total'].sum().sort_values(ascending=False)

print(reporte)
```
