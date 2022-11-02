# Elección del gestor de tareas.

Las opciones son Doit, Invoke y Pypyr.

- **Doit**  Tiene como idea usarse como un simple Task Runner que permita definir tareas 'ad hoc', unificando. Las dependencias y la creación de las tareas se pueden hacer dinámicamente durante su ejecución, lo que lo hace adecuado para conducir flujos de trabajo y pipelines complejas.

- **Invoke** Como bien se menciona [aquí](https://jj.github.io/curso-tdd/temas/gestores-tareas.html), en los gestores de tareas hay distintos tipos, entre los que nos fijamos entre estándar u opcionales. En el caso de python hace falta de una herramienta externa, como es el caso de invoke. Está inspirado en varias fuentes como make/rake entre otros y tiene así un conjunto de características potentes y limpias. Con invoke se puede definir y ejecutar funciones de tareas, crear pre-tareas, ejecutar comandos de shell entre otras opciones.

- **Pypyr** Permite definir y ejecutar pasos secuenciales en un pipeline. Como un script de shell ,más sencillo que un archivo MAKE. Ejecuta pipelines definidas en yaml. Da una sencilla sustitución de variables y gestión de archivos de configuración para que se pueda leer, fusionar y escribir archivos de configuración desde y hacia yaml, json o simplemente texto.

Se ha optado por **Invoke** por su simplicidad y documentación.