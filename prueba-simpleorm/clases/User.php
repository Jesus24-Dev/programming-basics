<?php

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