# :baggage_claim: User journey

___

**- Con qué frecuencia se usa.**
La idea es que reciba actualización diaria (o cada hora, esto tendría que valorarlo una vez entre en materia) de los datos meteorológicos, condiciones climáticas y estados de la zona en la que se encuentra el usuario para poder realizar los cálculos oportunos para poder estimar de manera más precisa el riesgo de incendio en las coordenadas en las que está el usuario final.

**- En qué contexto.**
En zonas forestales, principalmente, puesto que son las zonas que experimentan incendios.

**- Desde qué dispositivo.**
Principalmente, desde un teléfono, aunque puede ser también para ordenador.

**- Qué pasos tiene que dar para obtener la solución a su problema.**
   - Primero tener y entrenar una IA para poder establecer una fiabilidad de acierto alta, para ello se quiere utilizar datos recogidos [en esta página](http://archive.ics.uci.edu/ml/datasets/Forest+Fires).

   - Obtener datos del estado climático, estado de la zona, coordenadas del usuario y otros aspectos que se valorarán más tarde a la hora de hacer una IA que calcule la probabilidad.

   - Una vez con los datos extraídos y guardados en un formato útil para el estudio del riesgo, se usarán para hacer que la IA estime el riesgo de incendio.
   
   - Tras tener la estimación en caso de riesgo alto, notifica al usuario o mostrar solo el porcentaje o escala de riesgo de incendio.

___