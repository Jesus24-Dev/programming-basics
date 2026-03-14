# Idiorm
Idiorm es un micro-ORM (Object-Relational Mapper) construido sobre PDO. Su filosofía es la simplicidad absoluta:
- **Interfaz Fluida**: Escribes consultas encadenando métodos como si fuera lenguaje natural.
- **Sin Modelos**: A diferencia de otros ORM (como Eloquent), no necesitas crear una clase por cada tabla de tu base de datos. Simplemente le dices qué tabla quieres usar.
- **Protección SQL**: Usa sentencias preparadas automáticamente, protegiéndote contra inyecciones SQL.

## Configuracion base

```php
    require 'vendor/autoload.php';

    // Configuración de la conexión
    ORM::configure('mysql:host=localhost;dbname=mi_proyecto');
    ORM::configure('username', 'root');
    ORM::configure('password', '');

    // IMPORTANTE para SSR: Configurar Idiorm para devolver objetos manipulables
    ORM::configure('return_result_sets', true);
```

## Operaciones principales

### Lectura
Aquí recuperamos los datos y los mandamos a una vista.
```php
    Flight::route('GET /tasks', function() {
        // Buscamos todas las tareas en la DB
        $tasks = ORM::for_table('tasks')->find_many();

        // Renderizamos la vista 'tasks_list.php' pasando los objetos
        Flight::render('tasks_list', ['tasks' => $tasks]);
    });
```

En la vista (`tasks_list.php`):
```php
    <?php foreach($tasks as $task): ?>
        <li><?= htmlspecialchars($task->title) ?></li>
    <?php endforeach; ?>
```
### Creacion
En SSR, el cliente envía un formulario y el servidor lo procesa y redirecciona.

```PHP
    Flight::route('POST /tasks/save', function() {
        $title = Flight::request()->data->title;

        if (!empty($title)) {
            $task = ORM::for_table('tasks')->create();
            $task->title = $title;
            $task->save();
        }
        
        // Redireccionamos al listado (típico de SSR)
        Flight::redirect('/tasks');
    });
```

### Actualizacion 
Primero mostramos el formulario con los datos actuales y luego guardamos.

```php
    // 1. Mostrar el formulario de edición
    Flight::route('GET /tasks/edit/@id', function($id) {
        $task = ORM::for_table('tasks')->find_one($id);
        Flight::render('edit_form', ['task' => $task]);
    });

    // 2. Procesar el cambio
    Flight::route('POST /tasks/update/@id', function($id) {
        $task = ORM::for_table('tasks')->find_one($id);
        $task->title = Flight::request()->data->title;
        $task->save();
        
        Flight::redirect('/tasks');
});
```

### Eliminacion

```php
    // Procesar la eliminación
    Flight::route('POST /tasks/delete/@id', function($id) {
        // 1. Buscar el registro
        $task = ORM::for_table('tasks')->find_one($id);

        // 2. Si existe, eliminarlo
        if ($task) {
            $task->delete();
        }

        // 3. Redireccionar al listado principal (Patrón Post-Redirect-Get)
        Flight::redirect('/tasks');
    });
```

## Metodos clave

### for_table($table_name)
Es el punto de partida de cualquier operación. Indica a Idiorm sobre qué tabla de la base de datos vas a trabajar.

- Ejemplo: ORM::for_table('tasks')

### find_many()
Ejecuta la consulta y devuelve una colección (array) de objetos. Se usa cuando esperas múltiples resultados (como una lista de tareas).

- Ejemplo: $tasks = ORM::for_table('tasks')->find_many();

### find_one($id)
Busca un único registro. Si le pasas un argumento, lo buscará por su clave primaria (id). Si no pasas nada, devolverá el primer resultado que coincida con los filtros previos.

- Ejemplo: $task = ORM::for_table('tasks')->find_one(5);

### where($column, $value)
El filtro básico de igualdad. Equivale a WHERE columna = valor en SQL. Puedes encadenar tantos como necesites.

- Ejemplo: ->where('status', 'completed')

### create()
Prepara una nueva instancia de un objeto para ser insertada en la tabla. Es el primer paso para un Create en el CRUD.

- Ejemplo: $new_task = ORM::for_table('tasks')->create();

### save()
El método de persistencia más inteligente. Idiorm detecta automáticamente si el objeto es nuevo (ejecuta un INSERT) o si ya existía (ejecuta un UPDATE).

- Ejemplo: $task->title = 'Nueva Tarea'; $task->save();

### delete()
Elimina el registro actual de la base de datos. Se ejecuta sobre un objeto que ya ha sido recuperado previamente.

- Ejemplo: $task = ORM::for_table('tasks')->find_one(1); $task->delete();

### order_by_desc($column) / order_by_asc($column)
Define el orden de los resultados. En aplicaciones SSR es vital para mostrar, por ejemplo, los registros más recientes primero.

- Ejemplo: ->order_by_desc('created_at')

### limit($n) y offset($n)
Controlan la cantidad de registros y el punto de inicio. Son la base para construir cualquier sistema de paginación.

- Ejemplo: ->limit(10)->offset(20) (Muestra 10 registros saltándose los primeros 20).

### as_array()
Convierte el objeto "mágico" de Idiorm en un array asociativo estándar de PHP. Es imprescindible en SSR para pasar datos limpios a las vistas de FlightPHP.

- Ejemplo: Flight::render('lista', ['tasks' => $task->as_array()]);

## Flujo de un CRUD

|Operacion||Metodos Idiorm|
|:---:||:---:|
|Create||for_table, create, save|
|Read||for_table, find_many, where, as_array|
|Update||for_table, find_one, save|
|Delete||for_table, find_one, delete|