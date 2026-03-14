<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php if (!$editar): ?>
        <h2>Registro de usuario</h2>
        <form action="/crear" method="POST">
            <div>
                <label for="id">id</label>
                <input type="text" name="id" id="id">
            </div>
            <div>
                <label for="nombre">nombre</label>
                <input type="text" name="nombre" id="nombre">
            </div>
            <div>
                <label for="edad">edad</label>
                <input type="number" name="edad" id="edad">
            </div>
            <button type="submit">Crear</button>
        </form>
        <a href="/">Cancelar</a>
    <?php endif; ?>
    <?php if ($editar): ?>
        <h2>Edicion de usuario</h2>
        <form action="/editar/<?=$usuario->id?>" method="POST">
            <div>
                <label for="id">id</label>
                <input type="text" name="id" id="id" value=<?= htmlspecialchars($usuario->id) ?>>
            </div>
            <div>
                <label for="nombre">Nombre</label>
                <input type="text" name="nombre" id="nombre" value=<?= htmlspecialchars($usuario->nombre) ?>>
            </div>
            <div>
                <label for="edad">Edad</label>
                <input type="number" name="edad" id="edad" value=<?= htmlspecialchars($usuario->edad) ?>>
            </div>
            <button type="submit">Editar</button>
        </form>
        <a href="/">Cancelar</a>
    <?php endif; ?>
</body>
</html>