# :bookmark_tabs: Lista de comprobación: 

- :heavy_check_mark: ¿Se trata de un problema real del que se tenga conocimiento personal? <br/>
    
    Si, para poder trabajar y entrenar a una IA con deep learning se usarán datos de un csv recogido de los incendios ocurridos en la zona norte de [Portugal](http://archive.ics.uci.edu/ml/datasets/Forest+Fires). Con estos datos se pueden verificar si realmente están bien hecho las operaciones. 
    
    Los datos a utilizar tienen dos partes para poder entenderlo y diferenciarlo mejor:
    -  Datos a obtener: Estos datos son los esenciales para poder hacer operaciones y obtener a partir de ellos todos los datos necesarios para poder empezar a trabajar con la IA. Estos datos son la temperatura, viento, precipitaciones y humedad relativa.

    - Una vez se tienen estos datos se calculan los valores del [FWI](https://climate.copernicus.eu/fire-weather-index#:~:text=The%20Fire%20Weather%20Index%20(FWI,on%20fire%20behaviour%20and%20spread.), estos valores son DMC, DC, FFMC e ISI. 
    Para obtener estos datos hay dos vias posibles:
      - Calculando los valores manualmente por medio de código, estos cálculos se pueden consultar [aquí](https://wikifire.wsl.ch/tiki-index91f7.html?page=Fine+fuel+moisture+code)(En este enlace se muestra como calcular uno de ellos, es cuestión de hacerlo igual con los otros.)
      - Por otro lado, por medio de páginas que ya realizan estos cálculos directamente pasando los valores de temperatura, viento, precipitaciones y humedad relativa. Para esta opción sería hacer un script que accediese a la página y extrajera los datos, la cuál es la idea principal a hacer.


- :heavy_check_mark: ¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube? <br/>
    
    Sí, puesto que no se trata de un programa que se instala y ya, si no de un software que recoge datos, los procesa como se ha mencionado en el punto anterior y posteriormente con una IA usando deep learning estima el porcentaje de riesgo de incendio en la zona del cliente final, siendo la zona, zonas forestales.

- :heavy_check_mark: ¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?  <br/>
    
    Si, como se ha mencionado en el primer apartado, se tienen que recoger los datos básicos de la temperatura, viento, precipitaciones y humedad, una vez se han obtenido, usar una de las dos vias mencionadas, o haciendo los cálculos desde 0 con un programa u obteniéndolos directamente desde páginas que necesitas los 4 valores previos.
    Una vez obtenido todos los datos, se tiene que ir entrenando a la IA con deep learning. Los datos pueden ser verificados y así evitamos que no se sepa si son fiables o no estos cálculos. Es decir, todas las operaciones a realizar no son simplemente un busca en "x" página y actuliza en "y" con los datos de "x", se trata de un proceso de cierta cantidad de lógica.

- :heavy_check_mark: ¿Se ha incluído la configuración del repositorio y se ha enlazado desde el `README`?
    Si, se ha configurado correctamente con la clase de SSH
