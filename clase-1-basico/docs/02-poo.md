# Programacion Orientada a Objetos (POO)

La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el software en torno a "objetos" en lugar de funciones, modelando elementos del mundo real con atributos (datos) y métodos (comportamientos). Se basa en clases (plantillas) para crear instancias (objetos), facilitando el código reutilizable, modular y escalable.

## Clases e Instancias
- **Clase**: Es el "plano" o plantilla. Define qué datos tendrá un objeto y qué podrá hacer.
- **Instancia (Objeto)**: Es la materialización de la clase. Si "Coche" es la clase, "Tu Toyota rojo" es la instancia.

```php
    class Persona {
        // Clase vacía como plantilla
    }

    $juan = new Persona(); // $juan es una instancia (objeto) de Persona
```

## Atributos, metodos y constructor

- **Atributos**: Son variables que pertenecen a la clase (definen el estado).
- **Métodos**: Son funciones dentro de la clase (definen el comportamiento).
- **Constructor**: Es un método especial que se ejecuta automáticamente al crear un objeto. Se usa para inicializar los atributos.
  
```php
    class Mascota {
        public $nombre; // Atributo

        public function __construct($nombre) { // Constructor
            $this->nombre = $nombre;
        }

        public function comer() { // Método
            return $this->nombre . " está comiendo.";
        }
    }

    $perro = new Mascota("Bethoven");
    echo $perro->comer();
```

## Encapsulamiento (Metodos getters y setters)
Consiste en proteger los datos internos de un objeto para que no sean modificados de forma arbitraria. Usamos modificadores de acceso: public, protected y private

- **Public**: Acceso desde cualquier lugar.
- **Protected**: Acceso solo desde la misma clase o clases que hereden de ella.
- **Private**: Acceso únicamente dentro de la clase donde se definió.

```php
    class CuentaBancaria {
        private $saldo = 0; // Nadie puede tocarlo desde fuera

        public function depositar($cantidad) {
            if ($cantidad > 0) $this->saldo += $cantidad;
        }

        public function getSaldo() { // Getter
            return "$" . $this->saldo;
        }
    }

    $miCuenta = new CuentaBancaria();
    $miCuenta->depositar(100);
    echo $miCuenta->getSaldo(); // Correcto
    // echo $miCuenta->saldo; // ERROR: Es privado
```

## Herencia
Permite que una clase (hija) herede atributos y métodos de otra (padre), evitando repetir código.

```php
    class Animal {
        public function respirar() {
            return "Respirando...";
        }
    }

    class Gato extends Animal { // Hereda de Animal
        public function maullar() {
            return "Miau!";
        }
    }

    $michi = new Gato();
    echo $michi->respirar(); // Método heredado
```

## Abstracción
Se usa para definir clases "modelo" que no se pueden instanciar por sí mismas, sino que sirven para que otras hereden de ellas, obligándolas a implementar ciertos métodos.

```php
    abstract class Molde {
        abstract public function dibujar(); // Las hijas DEBEN tener este método
    }

    class Circulo extends Molde {
        public function dibujar() {
            return "Dibujando un círculo.";
        }
    }
```

## Polimorfismo
Es la capacidad de que diferentes clases respondan al mismo mensaje de formas distintas.

```php
    function hacerSonido(Animal $animal) {
        echo $animal->hablar();
    }

    // Diferentes clases con el mismo método "hablar"
    // Aunque se use la misma función, el resultado cambia según el objeto
```

## Metodos estaticos
Los métodos o propiedades estáticos pertenecen a la clase en sí, no a un objeto específico. Se acceden usando el operador de resolución de ámbito ::.

```php
    class Calculadora {
        public static $pi = 3.1416;

        public static function sumar($a, $b) {
            return $a + b;
        }
    }

    // No necesitamos hacer "new Calculadora()"
    echo Calculadora::$pi; 
    echo Calculadora::sumar(5, 10);
```