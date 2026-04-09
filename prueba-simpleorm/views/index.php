<h1>Usuarios</h1>
<a href="/create">Crear Usuario</a>

<ul>
<?php foreach ($users as $user): ?>
    <?php $role = $user->getRole(); ?>

    <li>
        <?= $user->name ?> - <?= $user->email ?>
        (<?= $role ? $role->name : 'Sin rol' ?>)

        <a href="/edit/<?= $user->id ?>">Editar</a>
        <a href="/delete/<?= $user->id ?>">Eliminar</a>
    </li>
<?php endforeach; ?>
</ul>