# 🧠 Guía básica de Git y GitHub

## 1. ¿Qué es Git y qué es GitHub?

- **Git** → sistema de control de versiones (trabaja en tu máquina).
- **GitHub** → plataforma en la nube para alojar repositorios Git.

👉 Git = cerebro

👉 GitHub = Dropbox con esteroides para código

---

## 2. Configuración inicial (primer paso obligatorio)

Después de instalar Git:

```bash
git config--global user.name"Tu Nombre"
git config--global user.email"tuemail@gmail.com"
git config --global core.editor "code --wait"
git config --global core.autocrlf true
```

Verifica:

```bash
git config--list
```

---

## 3. Crear un repositorio

### Opción A: Proyecto nuevo

```bash
git init
```

Esto crea un repositorio en la carpeta actual.

---

### Opción B: Clonar uno existente

```bash
git clone https://github.com/usuario/repositorio.git
```

---

## 4. Flujo básico (el 80% de Git)

Este es EL flujo que usarás todos los días:

```bash
git status# ver cambios
git add .# agregar cambios
git commit-m"mensaje"
git push# subir cambios
```

### 🧩 ¿Qué está pasando aquí?

1. `git add` → preparas archivos
2. `git commit` → guardas snapshot
3. `git push` → lo envías a GitHub

---

## 5. Estados de los archivos

Git maneja 3 estados:

- **Modified** → cambiaste algo
- **Staged** → listo para commit (`git add`)
- **Committed** → guardado en historial

---

## 6. Conectar con GitHub (repositorio remoto)

Primero crea un repo en GitHub.

Luego:

```bash
git remote add origin https://github.com/usuario/repositorio.git
git branch-M main
git push-u origin main
```

---

## 7. Traer cambios (pull)

```bash
git pull
```

👉 Esto descarga y mezcla cambios del remoto.

---

## 8. Ver historial

```bash
git log
```

Versión resumida:

```bash
git log--oneline
```

---

## 9. Ignorar archivos (.gitignore)

Ejemplo:

```bash
node_modules/
.env
dist/
```

👉 Evita subir basura o cosas sensibles.

---

## 10. Ramas (branches)

Crear una rama:

```bash
git branch nueva-rama
```

Cambiarte a ella:

```bash
git checkout nueva-rama
```

O en una sola línea:

```bash
git checkout-b nueva-rama
```

---

### Fusionar ramas

```bash
git checkout main
git merge nueva-rama
```

---

## 11. Revertir cambios (MUY importante)

### Descartar cambios no guardados:

```bash
git checkout-- archivo.txt
```

---

### Quitar archivo del stage:

```bash
git reset archivo.txt
```

---

### Volver a un commit anterior:

```bash
git reset--hard ID_DEL_COMMIT
```

⚠️ Esto borra cambios. No lo uses como loco.

---

## 12. Problema común: error de autenticación

GitHub ya no usa contraseña.

Debes usar:

- Token personal (PAT)
- o SSH

👉 Recomendación profesional: usa SSH.

---

## 13. Configurar SSH (recomendado)

Generar clave:

```bash
ssh-keygen-t ed25519-C"tuemail@gmail.com"
```

Mostrar clave:

```bash
cat ~/.ssh/id_ed25519.pub
```

La copias y la agregas en GitHub.

---

## 14. Buenas prácticas

- Commits claros:
    
    ```bash
    git commit-m"fix: corrige error en login"
    ```
    
- Haz commits pequeños (no monstruos de 2000 líneas)
- Usa ramas:
    - `feature/login`
    - `fix/navbar`

---

## 15. Mini flujo real (como dev profesional)

```bash
git checkout-b feature/login
# trabajas
git add .
git commit-m"feat: login básico"
git push origin feature/login
```

Luego haces Pull Request en GitHub.

---

## 16. Comandos esenciales resumidos

```bash
git init
git clone
git status
git add .
git commit-m""
git push
git pull
git branch
git checkout
git merge
git log
git reset
```