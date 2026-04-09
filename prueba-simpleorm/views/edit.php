<h1>Editar Usuario</h1>

<form method="POST" action="/update/<?= $user->id ?>">
    <input type="text" name="name" value="<?= $user->name ?>" required>
    <input type="email" name="email" value="<?= $user->email ?>" required>

    <select name="role_id">
        <?php foreach ($roles as $role): ?>
            <option value="<?= $role->id ?>"
                <?= $role->id == $user->role_id ? 'selected' : '' ?>>
                <?= $role->name ?>
            </option>
        <?php endforeach; ?>
    </select>

    <button type="submit">Actualizar</button>
</form>