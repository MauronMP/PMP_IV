

## Para qué se necesita un gestor de dependencias.

Como bien se menciona [aquí](https://ibm.github.io/data-science-best-practices/dependency_management.html)
> Dependency management is like your city’s sewage system. When it’s working well, it’s easy to forget that it even exists. The only time you’ll remember it is when you experience the agony induced by its failure.

Teniendo en cuenta el [estándar de la estructura de los proyectos en Python](https://docs.python-guide.org/writing/structure/) y [este ejemplo de estructura de proyectos](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

La estructura que buscamos tener sería:

- proyecto
    - LICENSE
    - pyproject.toml
    - README.md
    - src/
        - paquete_1
            - __init__.py
            - ejemplo.py
    - tests/
    - .gitignore
    - Makefile (en este caso el tasks.py con invoke que llama a poetry)

## Mejores prácticas para la gestión de dependencias de python.
- Debe de ser estable en todos los entornos en los que se trabaje. 
- Debe de ser fácil de instalar, compilar y ejecutar.
- Evitar el 'Dependency Hell', este concepto se asocia cuando se intenta resolver conflictos por dependencias. Esto ocurre cuando diferentes paquetes de Python tienen la misma dependencia, pero dependiendo de versiones distintas e incompatibles de un paquete compartido.
- Creación de un fichero lock, para asegurar que las dependencias sigan fijadas a las versiones exactas en uso.
- Tener todas las dependencias en un único fichero en lugar de tenerlo individualmente.

## Gestores de dependencias.

- **pip** Herramienta estándar para instalar paquetes de Python y administrar dependencias. Cuando se usa pip para instalar paquetes, recupera automáticamente el paquete y todas sus dependencias del Índice de paquetes de Python (PyPI) y los instala localmente en el sistema. Tiene la desventaja de que no resuelve los conflictos por dependencias. Usa un fichero.txt, en este caso requeriments.txt. Esto hace que todos los paquetes se guarden con versiones exactas, las actualizaciones tendrían que realizarse manualmente. A medida que avanza un proyecto es más lioso y se necesita de tiempo para mantener al día con los paquetes. En el caso de pip se usa un pipfile.lock, pero se usa con pipenv, que en este caso, no nos interesa. De igual modo, con pip se tiene que crear manualmente la estructura mencionada anteriormente como se puede ver [aquí](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

- **Conda** 
Es un paquete, dependencia y herramienta de gestión del entorno para Anaconda Python. Algunas de sus características básicas son similares a Pip, Virtualenv y Venv. Sin embargo, es una herramienta separada y mejorada diseñada para funcionar solo en entornos Conda.
Conda no solo proporciona entornos virtuales que aíslan o encajan cada proyecto para evitar conflictos de dependencia entre ellos; analiza cada paquete en busca de dependencias compatibles y posibles conflictos durante la instalación. Si hay un conflicto, Conda informa o indica que la instalación no se puede completar. No genera ficheros .lock, para ello se necesitaría de [conda lock](https://anaconda.org/conda-forge/conda-lock). Al crear un proyecto con Conda, no se sigue el estándar de los proyectos de python [aquí un ejemplo](https://anaconda-project.readthedocs.io/en/latest/user-guide/tasks/create-project.html)


- **poetry** Es una herramienta de dependencia y gestión de python, usa sistema de archivos de bloqueo para compiladores. Garantiza que se esté usando un entorno virtual, por lo que evita errores de instalaciones globales. Puede declarar sus dependencias por medio de la shell o en el fichero pyproject.toml
Las dependencias del proyecto se gestionan en el pyproject.toml, que se actualiza automáticamente cada vez que se ejecuta el comando de instalación de poetry. Genera del mismo modo un fichero lock. Tiende a ser más rápido. Sigue el estandar de la estructura de los projectos de python como se puede ver [en este ejemplo a la hora de crear un proyecto con poetry](https://python-poetry.org/docs/basic-usage/), ya que genera un fichero .toml, Readme.md, directorio para los .py y otro para los test.

Se ha optado por poetry por:

 - Seguir el estándar de la estructura de los proyectos en Python.
 - Documentación oficial muy sencilla.
 - Mejor visión de las dependencias al usar un fichero(pyproject.toml).
 - Tiene un entorno virtual integrado.
 - Construcción sencilla.
 - Permite cambiar fácilmente entre versiones.
 - Rendimiento.