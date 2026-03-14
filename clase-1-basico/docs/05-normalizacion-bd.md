# Base de datos y normalizacion

Una base de datos es una recopilacion de informacion o datos estructurados qeu se almacenan de manera digital.

## Tablas
Las tablas son estructuras que contienen los datos organizados en filas y columnas. Las filas representan un registro unico, y cada columna representa un campo dentro del registro.

## Claves
- **Clave primaria**: Es uno o mas valores de campo que hacen un registro unico
- **Clave foranea**: Es utilizada para referirse a un registro unico en otra tabla (utilizando la primaria de esa tabla)

## Normalizacion
La normalizacion es el proceso de eliminar la redundancia o de evitar la duplicidad en una base de datos.

### Primera Forma Normal (1FN): El fin de los grupos repetidos
Para que una tabla cumpla con la 1FN, debe cumplir tres reglas básicas:
- Cada columna debe contener un solo valor (valores atómicos). Nada de listas separadas por comas.
- No puede haber grupos de columnas que guarden datos similares (ej: Telefono1, Telefono2).
- Cada registro debe ser único mediante una clave primaria.

### Segunda Forma Normal (2FN): Dependencia Total
Para llegar aquí, primero debes cumplir la 1FN. La 2FN se enfoca en las tablas que tienen claves compuestas (una clave primaria formada por dos o más columnas).
- **La regla**: Todos los datos de la tabla deben depender de la clave completa, no solo de una parte de ella.
- **Ejemplo**: Si tienes una tabla Pedido_Producto con ID_Pedido e ID_Producto, y pones la Descripcion_Producto, esa descripción solo depende del producto, no del pedido. ¡Error! Debes mover la descripción a su propia tabla de Productos.

### Tercera Forma Normal (3FN): Fuera dependencias transitivas
Ya eres 1FN y 2FN. Ahora, la 3FN dice que las columnas que no son clave no deben depender de otras columnas que tampoco son clave.
- **La regla**: No debe haber dependencias transitivas. Es decir, si la columna A depende de la clave, y la columna B depende de A, entonces B no debería estar en esa tabla.
- **Ejemplo clásico**: En una tabla de Empleados, tienes el ID_Empleado, su nombre y el Codigo_Postal. Si añades una columna Ciudad, la ciudad depende del código postal, no directamente del empleado. Para cumplir la 3FN, mueves la ciudad a una tabla de Codigos_Postales.

## Relaciones
Las relaciones en una base de datos es el vinculo que se establece entre distintos elementos de las tablas que la conforman.

### Relacion uno a uno
Se realiza solo entre un registro de una tabla con un registro de otra. Es una de las relaciones mas utilizadas, ya que permiten una relacion de tipo exclusivo

### Relacion uno a varios
Un registro de una tabla puede enlazarse a varios registros de otra tabla. La primary key esta vinculada a varios registros de otra tabla

### Relacion muchos a muchos
Varios registros de una tabla pueden relacionarse con varios registros de otra tabla