# Conceptos Web

## ¿Qué es el internet?
El internet es una red global de computadoras interconectadas que permite a los usuarios compartir información y comunicarse entre sí. Funciona como una enorme telaraña digital que conecta miles de millones de dispositivos en todo el mundo, facilitando el acceso a una vasta cantidad de datos y servicios. El internet funciona dividiendo toda la información (como una página web, un video o un correo electrónico) en pequeños fragmentos llamados paquetes. Estos paquetes viajan a través de una compleja red de cables (fibra óptica, cobre) y ondas de radio (Wi-Fi) que conectan miles de millones de dispositivos en todo el mundo.

## ¿Qué es HTTP (y HTTPS)?
El HTTP (Hypertext Transfer Protocol) es el protocolo fundamental que permite la comunicación entre tu navegador web (el cliente) y el servidor donde está alojada una página web. Es como el "idioma" que usan para pedirse y enviarse información. Por otro lado, el HTTPS (Hypertext Transfer Protocol Secure) es la versión segura de HTTP. La "S" al final significa "Secure" (Seguro). HTTPS añade una capa de seguridad a la comunicación mediante el uso de cifrado SSL/TLS (Secure Sockets Layer/Transport Layer Security).

## ¿Qué son los métodos HTTP?
Los métodos HTTP, también conocidos como "verbos HTTP", son las acciones que un cliente (como tu navegador) le pide a un servidor que realice sobre un recurso específico (como una página web, una imagen, o un dato en una base de datos).

### Método GET
Se usa para solicitar o recuperar datos de un servidor. Es el método más común que se utiliza cuando navegas por internet. Cuando se escribe una URL en tu navegador, este envía una solicitud GET al servidor para obtener la página

### Método POST
Se usa para enviar datos a un servidor para que los procese, generalmente para crear un nuevo recurso o para enviar información de un formulario

### Método PUT
Se usa para actualizar o reemplazar completamente un recurso existente en el servidor, o crear uno nuevo si no existe con el identificador proporcionado.

### Método PATCH
Se usa para aplicar modificaciones parciales a un recurso existente. A diferencia de PUT, que envía la representación completa del recurso, PATCH envía solo los cambios que se quieren aplicar.

### Método DELETE
Se usa para eliminar un recurso específico del servidor.

## ¿Qué son los estados HTTP?
Los códigos de estado HTTP son números de tres dígitos que un servidor web envía como parte de su respuesta a una solicitud HTTP. Estos códigos indican el resultado de la operación solicitada por el cliente y le informan si la solicitud fue exitosa, si necesita más acciones o si hubo un error. Se agrupan en cinco clases, identificadas por el primer dígito:

### 2xx: Respuestas exitosas (Success)
Indican que la solicitud del cliente fue recibida, entendida y aceptada por el servidor. Son las respuestas ideales, significando que todo salió como se esperaba.

### 3xx: Redirecciones (Redirection)
Indican que es necesario tomar acciones adicionales para completar la solicitud. Esto suele significar que el recurso que se busca se ha movido o está disponible en otra ubicación.

### 4xx: Errores del cliente (Client Error)
Indican que hay un problema con la solicitud del cliente. El servidor no pudo procesar la solicitud debido a un error de sintaxis, una URL incorrecta, o porque el cliente no tiene permiso.

### 5xx: Errores del servidor (Server Error)
Indican que el servidor encontró un error mientras intentaba procesar una solicitud aparentemente válida. El problema no es del cliente, sino del servidor mismo.

Recurso: https://http.cat

## ARQUITECTURA CLIENTE-SERVIDOR
### ¿Qué es un cliente?
Un cliente es un programa o dispositivo que solicita y recibe servicios o recursos de otro programa o dispositivo. Por ejemplo: 
- Un navegador web (Chrome, Firefox, Safari) es un cliente que solicita páginas web a un servidor.
- Una aplicación de correo electrónico (Outlook, Gmail app) es un cliente que solicita y descarga tus correos de un servidor de correo.
- Un smartphone o computadora es un cliente cuando accede a una página web o usa una aplicación.
  
### ¿Qué es un servidor?
Un servidor es un programa o dispositivo que proporciona servicios o recursos a otros programas o dispositivos (los clientes).
- Un servidor web (donde está alojada una página) responde a las solicitudes del navegador y le envía la página web.
- Un servidor de correo electrónico almacena tus correos y los envía a la aplicación de correo cuando la abres.
- Un servidor de base de datos almacena información y la entrega a las aplicaciones que la solicitan.
  
### ¿En qué consiste el modelo Cliente-Servidor?
El modelo Cliente-Servidor es una arquitectura fundamental en la informática distribuida, incluyendo internet, que describe cómo interactúan diferentes programas o dispositivos. Es un sistema donde las tareas se dividen entre proveedores de recursos o servicios (servidores) y solicitantes de esos servicios (clientes). En este modelo, el cliente inicia la comunicación al enviar una solicitud a un servidor. El servidor, al recibir esa solicitud, la procesa y envía una respuesta de vuelta al cliente.

### ¿Qué es un endpoint?
Un endpoint (también conocido como punto final o punto de acceso) en el contexto de las APIs web (interfaces de programación de aplicaciones) es una URL específica (o URI) a la que un cliente puede acceder para interactuar con un recurso o realizar una acción en un servidor.
Por ejemplo, en una API para gestionar usuarios:
- https://api.ejemplo.com/usuarios podría ser un endpoint para obtener una lista de todos los usuarios (usando un método GET).
- https://api.ejemplo.com/usuarios/123 podría ser un endpoint para obtener los detalles del usuario con ID 123 (usando un método GET).
- https://api.ejemplo.com/usuarios (usando un método POST) podría ser para crear un nuevo usuario.
- https://api.ejemplo.com/usuarios/123 (usando un método DELETE) podría ser para eliminar al usuario con ID 123.

## ESTRUCTURA LÓGICA EN PROGRAMACIÓN WEB
En la estructura lógica de una aplicación web moderna (a menudo siguiendo patrones como MVC - Modelo-Vista-Controlador o arquitecturas de capas), cada componente tiene un rol específico para mantener el código organizado, modular y fácil de mantener.

### ¿Qué es un modelo?
Representa la lógica de negocio y los datos de la aplicación. Es la parte que interactúa directamente con la base de datos (o cualquier otra fuente de datos) para almacenar, recuperar, actualizar o eliminar información. El modelo no sabe nada de la interfaz de usuario ni de cómo se presentan los datos; solo se enfoca en la integridad y manipulación de los datos y las reglas del negocio.

### ¿Qué es un servicio?
Actúa como una capa intermedia entre el controlador y el modelo. Su función principal es encapsular la lógica de negocio más compleja que involucra múltiples modelos o coordinar varias operaciones de modelos para realizar una tarea específica. Los servicios promueven la reutilización de código y mantienen los controladores más limpios.

### ¿Qué es un controlador?
Es el intermediario que maneja las solicitudes del cliente. Recibe las peticiones HTTP (GET, POST, etc.) que llegan a la aplicación, interpreta qué se quiere hacer, coordina la interacción con los servicios (o directamente con los modelos si la lógica es simple) para obtener o manipular datos, y finalmente, decide qué respuesta enviar de vuelta al cliente (a menudo, renderizando una vista o enviando datos en formato JSON).

### ¿Qué es una ruta?
Define cómo las URLs de una aplicación se mapean a funciones específicas del código (generalmente a controladores). Es el mecanismo que le dice a la aplicación qué controlador debe manejar una solicitud HTTP en particular, basada en la URL y el método HTTP. Las rutas son como un "mapa" que guía las solicitudes entrantes al lugar correcto en la aplicación.

## TIPOS DE CONTENIDO WEB
### ¿Qué es la programación web?
La programación web es el campo de la informática que se encarga de crear y construir sitios web y aplicaciones que funcionan a través de internet. Su objetivo principal es permitir que los usuarios interactúen con información y servicios en línea. La programación web se divide principalmente en dos grandes áreas que trabajan de la mano:

#### Frontend
Se refiere a todo lo que el usuario ve y con lo que interactúa directamente en su navegador. Es la "cara" de la aplicación web. Consiste en el diseño, la estructura y la interactividad de una página web.

#### Backend
Se refiere a todo lo que sucede "detrás de escenas" en un servidor web y que el usuario no ve directamente. Es la "columna vertebral" de la aplicación. Se encarga de la lógica de negocio, la gestión de datos, la autenticación de usuarios y la comunicación con las bases de datos. Las tecnologías comunes incluyen lenguajes de programación como Python (con frameworks como Django o Flask), Node.js (JavaScript en el servidor), PHP, Ruby on Rails, Java, entre otros. También incluye las bases de datos (como MySQL, PostgreSQL, MongoDB) donde se almacena toda la información de la aplicación. Los desarrolladores backend se aseguran de que los datos se almacenen de forma segura, se procesen correctamente y se envíen al frontend cuando sea necesario.

## Server Side Rendering (SSR) y Client Side Rendering (CSR)
SSR (Server-Side Rendering) es una técnica de desarrollo web que genera el HTML completo de una página en el servidor antes de enviarlo al navegador. A diferencia del renderizado del lado del cliente (CSR), mejora el SEO y el rendimiento inicial al mostrar el contenido más rápido, siendo ideal para sitios web dinámicos.

El Client-Side Rendering (CSR) o renderizado del lado del cliente es una técnica de desarrollo web donde la mayor parte de la lógica, la obtención de datos y la creación de la interfaz de usuario ocurren directamente en el navegador del usuario utilizando JavaScript, en lugar de en el servidor.

## ¿Qué es una API?
Una API (Interfaz de Programación de Aplicaciones) es un conjunto de definiciones y protocolos que permite la comunicación e integración entre diferentes componentes de software. Sirve como un contrato que especifica cómo un componente de software (un cliente) debe interactuar con otro componente (un servidor) para solicitar funcionalidades o acceder a datos, sin necesidad de conocer los detalles internos de su implementación. Una API define formalmente:
- Operaciones disponibles: Qué acciones o funciones puede realizar el software que expone la API.
- Métodos de solicitud: Cómo se deben invocar esas operaciones (por ejemplo, a través de métodos HTTP como GET, POST, PUT, DELETE para APIs web).
- Estructuras de datos: El formato en que se deben enviar los datos en las solicitudes y el formato en que se recibirán las respuestas (comúnmente JSON o XML).
- Convenciones y reglas: Normas para la autenticación, manejo de errores, versionado y otras consideraciones técnicas.
