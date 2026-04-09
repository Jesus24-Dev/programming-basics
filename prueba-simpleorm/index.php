<?php

// Importa las clases esenciales. OJO, el orden es importante para evitar errores de clase no encontrada.
// Debes asegurarte de importar el ORM antes de las clases que lo utilizan
require 'orm/SimpleOrm.class.php';
require 'clases/User.php';
require 'clases/Role.php';
require 'flight/autoload.php';

Flight::set('flight.views.path', 'views');

//Configuras una conexion a la base de datos y se la asignas a SimpleORM para que pueda interactuar con ella.
//El orden es importante: primero el host,luego el usuario, la clave y por ultimo el nombre de la base de datos
$conn = new mysqli('localhost', 'root', '123456', 'crud_flightphp');

// Esto nos permite verificar la conexion
if ($conn->connect_error) {
    die('Error de conexión: ' . $conn->connect_error);
}

// Asignamos la conexión a SimpleORM para que pueda usarla en las operaciones de base de datos
SimpleOrm::useConnection($conn, 'crud_flightphp');

// LISTAR
Flight::route('/', function() {

//Aca mira como se usa el nombre de la clase para llamar a un metodo estatico que devuelve todos los 
// registros de la tabla asociada a esa clase. En este caso, User::all() devuelve todos los usuarios de la tabla 'users'.
    $users = User::all();

//Este metodo es similar al ORM::for_table('users')->find_many() que se usaria en Idiorm, pero adaptado a la sintaxis de SimpleORM.

    Flight::render('index', [
        'users' => $users
    ]);
});

// FORM CREAR
Flight::route('/create', function() {
    $roles = Role::all();

    Flight::render('create', [
        'roles' => $roles
    ]);
});

// GUARDAR
//Como hice las rutas con IA, veras que se incluyen el metodo POST y el request()->data;
//En tu caso, como no pide metodos http, asegurate de no colocar metodos y 
// recuperar los datos utilizando Flight::request()->query->nombre_del_campo
Flight::route('POST /store', function() {
    $name = Flight::request()->data->name;
    $email = Flight::request()->data->email;
    $role_id = Flight::request()->data->role_id;

    $user = new User();

    $user->name = $name;
    $user->email = $email;
    $user->role_id = $role_id;

    $user->save();

    Flight::redirect('/');
});

// FORM EDITAR
Flight::route('/edit/@id', function($id) {

    //El metodo retrieveByPk es un metodo estatico que se utiliza para recuperar un 
    // registro de la base de datos utilizando su clave primaria (primary key). 
    // En este caso, se esta recuperando un usuario por su id.
    $user = User::retrieveByPK($id);
    $roles = Role::all();

    Flight::render('edit', [
        'user' => $user,
        'roles' => $roles
    ]);
});

// ACTUALIZAR
Flight::route('POST /update/@id', function($id) {

    $name = Flight::request()->data->name;
    $email = Flight::request()->data->email;
    $role_id = Flight::request()->data->role_id;

    $user = User::retrieveByPK($id);

    if (!$user) {
        die("Usuario no encontrado");
    }

    // ✅ Asignación directa 
    $user->name = $name;
    $user->email = $email;
    $user->role_id = $role_id;

    $user->save();

    Flight::redirect('/');
});

// ELIMINAR
Flight::route('/delete/@id', function($id) {
    $user = User::retrieveByPK($id);

    if ($user) {
        $user->delete();
    }

    Flight::redirect('/');
});

Flight::start();