# Elección de la imagen de docker.

¿Qué se busca en una imagen?

- Tamaño de la imagen.
- Actualizado al día con el lenguaje, en este caso python.
- Actualizada las dependencias.

Partimos de dos caminos:

- **Oficiales de docker**

    - Alpine. Útil para imágenes pequeñas, pero puede conllevar a errores de rendimiento y tamaño por la gestión de paquetes.
    - Slim. Carece de las capas en los paquetes comunes, por lo que hace que sea una imagen mucho más pequeña.
    - Bullseye. Tiene muchos paquetes instalados por capas de imagen que usan otras imágenes de docker, lo que hace que el uso del disco sea bajo.

- **Otras**

    - Ubuntu. Imagen muy pesada en comparación con las anteriores y tiene muchos paquetes instalados que no son necesarios para este proyecto.
    - Debian. Más liviana que la anterior, pero para usar Debian es más conveniente usar una versión de las oficiales de python que usan Debian de manera más liviana, como el caso de la versión bullseye.
    - **bitnami** Esta será la elegida. Además de que es una imagen más ligera que las demás mencionadas, buen rendimiento, muchas descargas en dockerhub, cuenta además con el 'VERIFIED PUBLISHER' de dockerhub en python. Otro motivo ajeno es diferenciarse de las oficiales de python que serán elegidas por otros compañeros...

Finalmente, se ha elegido bitnami, en este caso la **3.9** ya que genera problemas con invoke, puesto que tanto invoke como nose2, opciones barajadas como tasks runners trabajan hasta las versiones 3.9 de python, pero las versiones de docker de python a partir de las 3.10 en adelante genera problemas por depenencias que los test runners no disponen. 
