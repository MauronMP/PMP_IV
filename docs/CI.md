Como parte del desarrollo del #7 y del objetivo 6, se tienen que elegir un sistema de integración continua.

## Criterios a tener en cuenta

- Gratuito o freemium
- Compatible con github check api.
- Pueda servir para poder testear lo realizado previamente con docker en el objetivo 5 y se puedan lanzar los tests con las distintas versiones.

## Algunos de los sistemas de integración continua:

- Github actions: Tiene un nivel gratuito, sirve con github check y es útil porque se puede usar con Docker y con python, la documentación además es muy extensa y buena.
- CircleCi: Compatible con muchos lenguajes, entre los cuales python, tiene como control de versiones Github, es una de las herramientas más tulizadas de DevOps, no es gratuita, pero ofrece un nivel gratuito que nos sirve para el desarrollo de la práctica.
- Jekins: Tiene el inconveniente de que requiere de una instalación de hardware propio, automatización de código abierto para integración continua, simple instalación y actualizaciones, pero es de pago si se quieren hacer scripts personalizados.
- AppVeyor: Compatible para python, sirve para entorno de trabajos como es el caso de Github, es gratuita para proyectos de código abierto, pero tiene un límite de 14 días.

Finalmente, se ha decidido por emplear CircleCI con docker y Github Actions para el control de versiones del proyecto.