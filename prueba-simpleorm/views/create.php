<h1>Crear Usuario</h1>

<form method="POST" action="/store">
    <input type="text" name="name" required placeholder="Nombre">
    <input type="email" name="email" required placeholder="Email">

    <select name="role_id">
        <?php foreach ($roles as $role): ?>
            <option value="<?= $role->id ?>">
                <?= $role->name ?>
            </option>
        <?php endforeach; ?>
    </select>

    <button type="submit">Guardar</button>
</form>