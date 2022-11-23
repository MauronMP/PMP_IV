# Elección de la imagen de docker.

¿Qué se busca en una imagen?

- Estabilidad.
- Tamaño de la imagen.
- Actualizado al día con el lenguaje, en este caso python.
- Actualizada las dependencias.

Partimos de dos caminos:

- **Oficiales de docker**

    - Alpine. Útil para imágenes pequeñas pero puede conllevar a errores de rendimiento y tamaño por la gestión de paquetes.
    - Slim. Carece de las capas en los paquetes comunos por lo que hace que sea una imagen mucho más pequeña.
    - Bullseye. Tiene muchos paquetes instalados por capas de imagen que usan otras imágenes de docker, lo que hace que el uso del disco sea bajo.

- **Otras**

    - Ubuntu. Imagen muy pesada en comparación con las anteriores y tiene muchos paquetes instalados que no son necesarios para este proyecto.
    - Debian. Más liviana que la anterior, pero para usar Debian es más conveniente usar una versión de las oficiales de python que usan Debian de manera más liviana como el caso de la versión bullseye.

Finalmente se ha elegido la oficial de docker, en este caso la la [3.8-slim-buster](https://github.com/docker-library/python/blob/d24131ca9b820cd7a83ec7920b49bd0463d4db92/3.8/slim-buster/Dockerfile)
