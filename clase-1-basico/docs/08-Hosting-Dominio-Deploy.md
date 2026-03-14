# Hosting, Dominio, Deploy

## El Dominio: Tu dirección en la web
El dominio es el nombre único y exclusivo que se le asigna a tu sitio web para que los usuarios puedan visitarlo.
- **¿Para qué sirve?** Traduce las direcciones IP (que son números complejos como 192.168.1.1) en palabras fáciles de recordar (como google.com).
- **Partes de un dominio**: Se compone del nombre (ej. "miempresa") y la extensión o TLD (ej. ".com", ".org", ".net").
- **Dato clave**: Los dominios se alquilan anualmente a través de un "Registrar" y, una vez que lo tienes, nadie más puede usar ese nombre exacto.

## El Hosting: El espacio donde vive tu web
El hosting (o alojamiento web) es el servicio de almacenamiento que guarda todos los archivos de tu sitio (imágenes, código HTML, bases de datos, videos) en un servidor conectado a internet las 24 horas. Existen diferentes tipos según tus necesidades:
- **Hosting Compartido**: Como vivir en un edificio de apartamentos; compartes recursos (agua, luz) con otros vecinos. Es el más económico.
- **VPS (Servidor Privado Virtual)**: Tienes tu propio espacio reservado dentro de un servidor compartido. Más control y potencia.
- **Hosting Dedicado**: Tienes un servidor entero para ti solo. Es para sitios con tráfico masivo.
- **Cloud Hosting**: Tu sitio se distribuye en varios servidores interconectados, lo que lo hace muy estable.

## El Deploy: El acto de "lanzar" tu proyecto
El deploy (o despliegue) es el proceso de trasladar el código que un programador escribió en su computadora personal hacia el servidor de hosting para que esté disponible en vivo.
- **¿En qué consiste?** No es solo "subir archivos". Implica configurar la base de datos, instalar dependencias, compilar el código y asegurarse de que el entorno del servidor sea compatible con la aplicación.
- **Integración Continua (CI/CD)**: Hoy en día, muchas empresas usan herramientas que hacen el deploy automáticamente cada vez que el programador guarda un cambio importante.