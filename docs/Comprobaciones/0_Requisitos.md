# :bookmark_tabs: Lista de comprobación: 

- :heavy_check_mark: ¿Se trata de un problema real del que se tenga conocimiento personal? <br/>
    
    Si, la idea es trabajar con los datos de un csv de la zona norte de [Portugal](http://archive.ics.uci.edu/ml/datasets/Forest+Fires). Con estos datos se pueden verificar si realmente están bien hecho las operaciones. 
    
    La idea principal es poder obtener a partir de los datos anteriores un nivel de riesgo con un porcentaje de precisión relativamente decente. Los datos que se usan además de ser buenos, son datos que se emplean en el estudio de riesgo de incendios, estos datos son los del [FWI](https://climate.copernicus.eu/fire-weather-index#:~:text=The%20Fire%20Weather%20Index%20(FWI,on%20fire%20behaviour%20and%20spread.). 

    Con los datos se pretende aplicar algoritmos que se han detallado en los milestone para determinar en la zona a*b el nivel de riesgo de incendio. 
    El nivel de riesgo de incendio se ha detallado de igual modo en los milestone estudiando los vecinos del perímetro. Igualmente se quiere poder determinar el grado de incendio de manera aceptable. 


- :heavy_check_mark: ¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube? <br/>
    
    Sí, puesto que no se trata de un programa que se instala y ya, si no de un software que procesa datos y estima el porcentaje de riesgo de incendio en la zona y el nivel de incendio.

- :heavy_check_mark: ¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?  <br/>
    
   Si, ya que se necesita un proceso de transformación, validación y estudio para poder hacer estimación del nivel de incendio con un porcentaje de acierto aceptable y no se trata de consultar una fichero y hacer búsquedas simples.

- :heavy_check_mark: ¿Se ha incluído la configuración del repositorio y se ha enlazado desde el `README`?
    Si, se ha configurado correctamente con la clase de SSH
