<?php

require 'vendor/autoload.php';

//Configuracion inicial del ORM

ORM::configure('mysql:host=localhost;dbname=registro');
ORM::configure('username', 'root');
ORM::configure('password', '');
ORM::configure('return_result_sets', true);

//Setea la carpeta de vistas
Flight::set('flight.views.path', 'views');

//Ruta de inicio
//Lectura
Flight::route('GET /', function () {
    $usuarios = ORM::for_table('usuarios')->find_many();
    Flight::render('inicio', ['usuarios' => $usuarios]);
});

//Crear
Flight::route('GET /crear', function() {
    Flight::render("formulario", ['editar' => false]);
});

Flight::route('POST /crear', function() {
    $data = Flight::request()->data;
    $usuario = ORM::for_table('usuarios')->create();
    $usuario->id = $data->id;
    $usuario->nombre = $data->nombre;
    $usuario->edad = $data->edad;
    $usuario->save();

    Flight::redirect("/");
});

//Actualizar
Flight::route('GET /editar/@id', function($id) {
    $usuario = ORM::for_table('usuarios')->find_one($id);
    Flight::render("formulario", ['editar' => true, 'usuario' => $usuario]);
});

Flight::route('POST /editar/@id', function($id) {
    $data = Flight::request()->data;
    $usuario = ORM::for_table('usuarios')->find_one($id);
    $usuario->id = $data->id;
    $usuario->nombre = $data->nombre;
    $usuario->edad = $data->edad;
    $usuario->save();
    Flight::redirect("/");
});

//Eliminar
Flight::route('POST /eliminar/@id', function($id) {

    $usuario = ORM::for_table('usuarios')->find_one($id);

    if ($usuario) {
        $usuario->delete();
    }

    Flight::redirect("/");
});

Flight::start();