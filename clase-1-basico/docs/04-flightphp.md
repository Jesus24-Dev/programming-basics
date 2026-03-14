# FlightPHP
Flight es un microframework extensible. Su filosofía es darte las herramientas mínimas necesarias (enrutamiento, renderizado, manejo de peticiones) para que tú construyas el resto. Es ideal para construir REST APIs rápidas o aplicaciones web sencillas donde el rendimiento es crítico.

## Características principales:
- **Ligero**: El núcleo ocupa muy poco espacio.
- **Sin dependencias externas**: No te obliga a usar librerías que no quieres.
- **Flexible**: Puedes registrar tus propias clases y métodos.
  
## Arquitectura de la Aplicación
Flight no impone una estructura de carpetas rígida como el patrón MVC tradicional, pero permite implementarlo fácilmente. Su flujo de trabajo se basa en:

- Punto de entrada: Un archivo index.php donde se centralizan las rutas.
- Enrutamiento: Mapeo de URLs a funciones o métodos de clase.
- Contenedor de Servicios: Permite registrar componentes (Base de datos, motores de plantillas) para usarlos globalmente.

## Estructura Principal del `index.php`
```php
<?php
    // 1. Carga del Autoloader (Fundamental para que Flight funcione)
    require 'vendor/autoload.php';

    // 2. Configuración y Registro de Componentes (Base de datos, variables globales)
    Flight::set('flight.views.path', 'views'); // Opcional: define la carpeta de vistas
    Flight::register('db', 'PDO', ['mysql:host=localhost;dbname=test', 'user', 'pass']);

    // 3. Definición de Rutas (El mapa de tu aplicación)
    Flight::route('/', function() {
        echo '¡Hola Mundo!';
    });

    // 4. Encendido del Motor (Siempre debe ir al final)
    Flight::start();
```

## Vistas y Carpeta `views/`
Flight busca por defecto los archivos de interfaz en una carpeta llamada views/ (al mismo nivel que tu `index.php`).

### ¿Cómo retornar una vista?
Se utiliza el método `Flight::render()`. Por defecto, Flight asume que tus archivos tienen la extensión `.php`.

#### Creacion de archivo `views/perfil.php`
```php
    <h1>Hola, <?= $nombre ?></h1>
    <p>Tu ID es: <?= $id ?></p>
```

#### Retorno en el `index.php`
```php
    Flight::route('/usuario/@id', function($id) {
        // El segundo parámetro es un array asociativo con los datos para la vista
        Flight::render('perfil', ['nombre' => 'Juan', 'id' => $id]);
    });
```

## Estructura de rutas
Las rutas en Flight son potentes y flexibles. Se definen mediante `Flight::route(cadena, funcion)`.

### Metodos HTTP
Puedes especificar qué método aceptar anteponiéndolo a la ruta:
```php
    Flight::route('GET /tareas', function() { /* Listar */ });
    Flight::route('POST /tareas', function() { /* Crear */ });
```

### Parametros dinamicos 
Se definen con el símbolo @. Flight pasará automáticamente estos valores como argumentos a tu función:
```php
    Flight::route('/producto/@nombre/@color', function($nombre, $color) {
        echo "Estás viendo el producto: $nombre de color $color";
    });
```

### Parametros opcionales y comodines
Si quieres que un parámetro sea opcional, usa el signo (? ... ):
```php
    // Acepta /blog y /blog/1
    Flight::route('/blog(/@pagina)', function($pagina) {
        echo "Viendo página: " . ($pagina ?? 1);
    });
```

### Agrupacion (Rutas con prefijo)
Para organizar mejor un CRUD, puedes usar el encadenamiento o simplemente organizar por nombres:

```php
    Flight::group('/api/v1', function() {
        Flight::route('GET /users', function() { ... });
        Flight::route('GET /posts', function() { ... });
    });
```