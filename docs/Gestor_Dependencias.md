# Elección del gestor de dependencias.

Teniendo en cuenta [el issue](https://github.com/MauronMP/PMP_IV/issues/17) y la [HU0](https://github.com/MauronMP/PMP_IV/issues/7) #7, se quiere elegir un gestor de dependencias como parte del objetivo 3.

Hay distintas opciones para el gestor de dependencias:


- **poetry** Es una herramienta de dependencia y gestión de python, usa sistema de archivos de bloqueo para compiladores. Garantiza que se esté usando un entorno virtual, por lo que evita errores de instalaciones globales. Puede declarar sus dependencias por medio de la shell o en el fichero pyproject.toml
- **pip-tools** Usado para el manejo de dependencias, basado en dos comandos, 'pip-compile' y 'pip-sync', uno crea un fichero de requerimientos y otro instala las cosas del primero. Pero se usa el fichero requeriments.txt lo cúal hace que todos los paquetes se guarden con versiones exactas, las actualizaciones tendrían que realizarse manualmente. A medida que avanza un proyecto es más lioso y se necesita de tiempo para mantener al día con los paquetes.
- **pipenv** Usando para el manejo de versiones de python. Su últilma actualización es de finales de 2018. Al igual que el anterior, se usa un "requeriments.txt" y genera los problemas del anterior.

Se ha optado por poetry por:
 - Mejor visión de las dependencias al usar un fichero(pyproject.toml).
 - Tiene un entorno virtual integrado.
 - Construcción sencilla.
 - Permite cambiar fácilmente entre versiones.
 - Rendimiento.