# Elección de una biblioteca de aserción.

Vamos a partir de las valoraciones de [esta página](https://snyk.io/advisor/python). Que hace una comparativa de cada librería para un proyecto para distintos lenguajes, en este caso python. La manera de evaluar cómo de bueno es un paquete es por:
- Popularidad.
- Mantenimiento.
- Seguridad.
- Comunidad.

## **Opciones**.


- **grappa** Tiene como finalidad hacer que las pruebas sean más sencillas. Tiene dos tipos de asserciones: "expect y should". Tiene un sistema detallado de informes de errores "amigable". Pero tiene una mala valoración y apenas hay documentación o ejemplos además de la oficial.

- **assertpy** Tiene un buen soporte para poder trabajar con estructuras nativas de python como list, set o dict entre otros. Tiene personalización de los mensajes de aserciones, aunque la valoración que tiene sigue siendo mala, aunque mejor que la anterior.


- **:checkered_flag: pyhamcrest** Permite definir de manera clara las reglas, tiene un buen manejo de los mensajes de errores y ayuda así a una mejor comprensión. Tiene una amplia documentación y cuenta con muchos "[matchers](https://pyhamcrest.readthedocs.io/en/release-1.8/tutorial/#predefined-matchers)" predefinidos.

