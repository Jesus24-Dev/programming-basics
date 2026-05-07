import pandas as pd

df = pd.read_csv('ventas_tecnologia.csv')

# imprimir las primeras 3 filas
print('--- Primeras 3 filas---')
# print(df.head(3))

# seleccionar solo la columna 'producto'
solo_nombres = df['producto']
print('\n--- Lista de productos ---')
# print(solo_nombres)

# filtrar productos de mas de 500usd
ventas_caras = df[df['precio_unitario'] > 500]
print('\n--- Ventas de lujo ---')
# print(ventas_caras)

# creando columna subtotal
df['subtotal'] = df['cantidad'] * df['precio_unitario']
print('\n--- Nueva Columna Subtotal ---')
# print(df)

# ordenando desde el mas costoso
df_ordenado = df.sort_values(by='precio_unitario', ascending=False)
print('\n--- Productos desde el mas costoso ---')
# print(df_ordenado)

df_favoritos = df[(df['cantidad'] > 1) & (df['categoria'].str.lower() == 'accesorios')]
print('\n--- Productos favoritos ---')
# print(df_favoritos.to_string())

# limpiando registros con valores nulos en precio_unitario 
df_limpio = df.dropna(subset=('precio_unitario'))
print('\n--- Productos limpios ---')
# print(df_limpio)

df_suma_por_categoria = df.groupby('producto')['subtotal'].sum()
print('\n--- Productos limpios ---')
# print(df_suma_por_categoria)

transacciones = df['producto'].value_counts()
print('\n--- Transacciones por producto ---')
# print(transacciones)

promedio = df['precio_unitario'].mean()
print(f"El precio promedio de los productos es: {promedio:.2f}")
