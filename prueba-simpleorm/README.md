# Explicacion

Primero, instala la extension **Markdown Preview Enhanced** para que puedas observar correctamente

## Carpeta /clases
Aqui estan las clases de la base de datos, tienes dos, una de usuario y una con roles. Para las relaciones entre tablas debes forzar la relacion (tal como esta en la tabla usuario)

```php
class User extends SimpleOrm {
    protected static
        $table = 'users';

        //Forzar la modificacion
    protected $isModified = true;

    // Relación manual (SimpleORM no la maneja automáticamente)
    public function getRole() {
        return Role::retrieveByPK($this->role_id);
    }
}
```

## Carpeta /flight
Ya tu sabes, flightphp

## Carpeta /orm
Aca se encuentra **SimpleORM**, dentro encontraras un archivo `README.md` donde explica como funciona y como utilizarlo.

## Carpeta /views
Igual que los demas, aca estan las vistas

## Archivo `database.sql`
El script de la base de datos a utilizar (para este ejemplo)

## Archivo `index.php`
El archivo donde esta el index de la aplicacion y la configuracion inicial, junto a las rutas.