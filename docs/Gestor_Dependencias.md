# Eleción del gestor de dependencias.

Teniendo en cuenta [el issue](https://github.com/MauronMP/PMP_IV/issues/17) y la [HU0](https://github.com/MauronMP/PMP_IV/issues/7) #7, se quiere elegir un gestor de dependencias como parte del objetivo 3.

Hay distintas opciones para el gestor de dependencias:
- **venv.**  Es una parte de la librería estándar de python, en caso de tener una versión superior a la 3.3, ya se tiene instalado. Usa un entorno virtual que incluye su propia instalación de python.
- **pipenv** Usando para el manejo de versiones de python. Su últilma actualización es de finales de 2018.
- **poetry** Es una herramienta de dependencia y gestión de python, usa sistema de archivos de bloqueo para compiladores. Garantiza que se esté usando un entorno virtual, por lo que evita errores de instalaciones globales. Puede declarar sus dependencias por medio de la shell o en el fichero pyproject.toml
- **pip-tools** Usado para el manejo de dependencias, basado en dos comandos, 'pip-compile' y 'pip-sync', uno crea un fichero de requerimientos y otro instala las cosas del primero.

Se ha optado por poetry por:
 - Mejor visión de las dependencias al usar un fichero(pyproject.toml).
 - Tiene un entorno virtual integrado.
 - Construcción sencilla.
 - Permite cambiar facilmente entre versiones.
 - Rendimiento.