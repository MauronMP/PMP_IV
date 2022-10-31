# Elección del gestor de tareas.

Teniendo en cuenta [el issue](https://github.com/MauronMP/PMP_IV/issues/18) y la [HU0](https://github.com/MauronMP/PMP_IV/issues/7) #7, se quiere elegir un gestor de tareas como parte del objetivo 3.

El gestor de tareas elegido es [invoke](https://www.pyinvoke.org).
Como bien se menciona [aquí](https://jj.github.io/curso-tdd/temas/gestores-tareas.html), en los gestores de tareas hay distintos tipos, entre los que nos fijamos entre estándar u opcionales. En el caso de python hace falta de una herramienta externa, como es el caso de invoke.

Está inspirado en varias fuentes como make/rake entre otros y tiene así un conjunto de características potentes y limpias.

Con invoke se puede definir y ejecutar funciones de tareas, crear pre-tareas, ejecutar comandos de shell entre otras opciones.