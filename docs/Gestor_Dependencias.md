

## Para qué se necesita un gestor de dependencias.

Como bien se menciona [aquí](https://ibm.github.io/data-science-best-practices/dependency_management.html)
> Dependency management is like your city’s sewage system. When it’s working well, it’s easy to forget that it even exists. The only time you’ll remember it is when you experience the agony induced by its failure.

Teniendo en cuenta el [estándar de la estructura de los proyectos en Python](https://docs.python-guide.org/writing/structure/) y [este ejemplo de estructura de proyectos](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

La estructura que buscamos tener sería:

- proyecto
    - pyproject.toml
    - README.md
    - proyecto/
        - __init__.py
    - tests/
        - __init__.py

> Por favor no copiéis ni esto ni la lista de gestores que se han puesto aquí. Buscad los vuestros propios, porque se trata de que tratéis de encontrar la solución a los problemas que se plantean en vuestro proyecto.

## Mejores prácticas para la gestión de dependencias de python.
- Debe de ser estable en todos los entornos en los que se trabaje. 
- Debe de ser fácil de instalar, compilar y ejecutar.
- Evitar el 'Dependency Hell', este concepto se asocia cuando se intenta resolver conflictos por dependencias. Esto ocurre cuando diferentes paquetes de Python tienen la misma dependencia, pero dependiendo de versiones distintas e incompatibles de un paquete compartido.
- Creación de un fichero lock, para asegurar que las dependencias sigan fijadas a las versiones exactas en uso.
- Tener todas las dependencias en un único fichero en lugar de tenerlo individualmente.
- Seguir el estándar de [PEP 518](https://peps.python.org/pep-0518/).
- En este caso seguir el estándar [PEP 621](https://peps.python.org/pep-0621/) para el fichero pyproject.toml

## Gestores de dependencias.

- **PDM** Instala y gestiona paquetes de manera similar a npm que no necesita crear un virtualenv. Soporta el PEP 582, sigue los estándares de python. Sistema flexible y potente. Cache de instalación centralizado como pnpm. De igual modo, a la hora crear un proyecto sigue el estándar y genera una [estructura útil](https://pdm.fming.dev/latest/usage/project/)


- **hatch** Es una herramienta útil para el aislamiento del entorno y destinado a administrar dependencias. Tiene un sistema de complementos que hace fácil su funcionalidad. Sistema de compilación estandarizado con compliaciones de manera predeterminada. [Sigue el estándar de la estructura de proyectos](https://hatch.pypa.io/latest/intro/).


- **poetry** Es una herramienta de dependencia y gestión de python, usa sistema de archivos de bloqueo para compiladores. Garantiza que se esté usando un entorno virtual, por lo que evita errores de instalaciones globales. Puede declarar sus dependencias por medio de la shell o en el fichero pyproject.toml
Las dependencias del proyecto se gestionan en el pyproject.toml, que se actualiza automáticamente cada vez que se ejecuta el comando de instalación de poetry. Genera del mismo modo un fichero lock. Tiende a ser más rápido. Sigue el estandar de la estructura de los projectos de python como se puede ver [en este ejemplo a la hora de crear un proyecto con poetry](https://python-poetry.org/docs/basic-usage/), ya que genera un fichero .toml, Readme.md, directorio para los .py y otro para los test.

Se ha optado por poetry por:

 - Seguir el [estándar](https://peps.python.org/pep-0518/) de la 'Specifying Minimum Build System Requirements for Python Projects'.
 - Documentación oficial muy sencilla.
 - Mejor visión de las dependencias al usar un fichero(pyproject.toml).
 - Tiene un entorno virtual integrado.
 - Construcción sencilla.
 - Permite cambiar fácilmente entre versiones.
 - Rendimiento.
