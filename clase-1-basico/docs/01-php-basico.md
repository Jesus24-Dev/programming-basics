# PHP Básico
## ¿Qué es PHP?
PHP (Hypertext Preprocessor) es un lenguaje de scripting de código abierto que se ejecuta en el servidor. A diferencia de JavaScript (que corre en el navegador del usuario), PHP prepara el contenido en el servidor y envía al cliente solo el código HTML resultante.

### Conceptos Clave
- **Interpretado**: El código se ejecuta línea por línea sin necesidad de una compilación previa compleja.
- **Débilmente tipado**: No necesitas declarar estrictamente el tipo de dato de una variable; PHP lo deduce según el contexto.
- **Embebido**: Puedes mezclar PHP directamente dentro de etiquetas HTML usando <?php ... ?>.

## Variables y Tipos de Datos
Las variables en PHP siempre comienzan con el signo $.
- **Básicos**: boolean (true/false), integer (enteros), float (decimales), string (cadenas de texto).
- **Compuestos**: array (colecciones), object (instancias de clases).
- **Especiales**: NULL (variable vacía) y resource (referencias externas como conexiones a bases de datos).

```php
    <?php
    $texto = "Hola Mundo";        // String
    $entero = 2026;               // Integer
    $decimal = 9.5;               // Float
    $esVerdad = true;             // Boolean

    echo "El año es $entero y el mensaje es: $texto"; 
    ?>
```

## Entrada y Salida
- **Salida**: Lo más común es echo (rápido y simple) o print.
- **Entrada**: En entornos web, la entrada no es por teclado (como en C++), sino a través de parámetros HTTP mediante las superglobales $_GET, $_POST o $_FILES.

```php
    // Imagina que un usuario envía un formulario con un campo 'nombre'
    $nombreUsuario = $_POST['nombre'] ?? 'Invitado'; // Entrada (POST)

    echo "<h1>Bienvenido, " . $nombreUsuario . "</h1>"; // Salida (HTML)
```
  
## Condicionales (Lógica de Decisión)
Controlan el flujo del programa basándose en comparaciones lógicas.
- **if / elseif / else**: Para decisiones basadas en condiciones verdaderas.
- **switch**: Ideal para comparar una sola variable contra múltiples valores posibles.

```php
    $hora = 14;

    if ($hora < 12) {
        echo "Buenos días";
    } elseif ($hora < 19) {
        echo "Buenas tardes";
    } else {
        echo "Buenas noches";
    }
```
  
## Ciclos (Lógica de Repetición)
- **for**: Cuando sabes cuántas veces se debe repetir el proceso.
- **while**: Se repite mientras una condición sea cierta.
- **foreach**: La joya de PHP; diseñado específicamente para recorrer arreglos de forma sencilla.

```php
    $frutas = ["Manzana", "Banana", "Cereza"];

    // Ciclo For clásico
    for ($i = 0; $i < count($frutas); $i++) {
        echo "Fruta $i: " . $frutas[$i] . "<br>";
    }

    // Ciclo Foreach (más limpio para arreglos)
    foreach ($frutas as $fruta) {
        echo "Me gusta la $fruta <br>";
    }
```
  
## Funciones
Son bloques de código reutilizables. PHP permite pasar argumentos por valor o por referencia y definir tipos de retorno para dar más robustez al código.

```php
    function calcularIva($precio, $tasa = 0.16) {
        $total = $precio + ($precio * $tasa);
        return $total;
    }

    echo "Total con IVA: " . calcularIva(100); // Salida: 116
```

## Arreglos (Arrays)
En PHP, los arreglos son increíblemente versátiles. Pueden ser:

- **Indexados**: Acceso por número (0, 1, 2...).
- **Asociativos**: Usan "claves" de texto en lugar de números (ej: 'nombre' => 'Juan').
- **Multidimensionales**: Arreglos dentro de otros arreglos.
  
```php
    // Arreglo Asociativo
    $usuario = [
        "id" => 1,
        "nombre" => "Carlos",
        "rol" => "Admin"
    ];

    echo "El administrador es: " . $usuario["nombre"];
```

## Clases y Objetos (POO)
PHP moderno es orientado a objetos. Una Clase es el plano o molde, y el Objeto es la casa construida.

- **Propiedades**: Variables dentro de la clase.
- **Métodos**: Funciones dentro de la clase.
- **Constructor**: Un método especial (__construct) que se ejecuta automáticamente al crear el objeto.

```php
    class Coche {
        public $marca;
        public $color;

        public function __construct($marca, $color) {
            $this->marca = $marca;
            $this->color = $color;
        }

        public function encender() {
            return "El $this->marca de color $this->color ha arrancado.";
        }
    }

    // Instanciar el objeto
    $miCoche = new Coche("Toyota", "Rojo");
    echo $miCoche->encender();
```