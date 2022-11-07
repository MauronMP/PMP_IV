# Elección de un test runner.

Vamos a partir de las valoraciones de [esta página](https://snyk.io/advisor/python). Que hace una comparativa de cada librería para un proyecto para distintos lenguajes, en este caso python. La manera de evaluar cómo de bueno es un paquete es por:
- Popularidad.
- Mantenimiento.
- Seguridad.
- Comunidad.

## **Opciones**.

- **:checkered_flag: PyTest**  Partiendo que tiene [la mejor valoración](https://snyk.io/advisor/python/pytest). Se usará este con un plugin llamado pytest-tap que genera los test que se realizen en formato TAP para así seguir el estándar. Tiene como características la búsqueda automática de ficheros con nombre "test" o sufijo "_test.py", la creación de los test es bastante sencilla, permite parametrización, tiene Hooks que son útiles en las fases de setup y teardown.

- **Nose2** EL sucesor de nose, [tiene buena valoración, pero es menor](https://snyk.io/advisor/python/nose2) que la de pytest. Basado en unittest2 con mejores opciones de testeo, en este caso solo ejecutará los ficheros que empiecen por "test_". Tiene menos popularidad, soporte y es como una "extensión mejorada" de unittest.