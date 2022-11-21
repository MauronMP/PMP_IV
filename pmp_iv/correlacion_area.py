from math import *

class correlacion_area():
    
    def __init__(self, propiedad, area_quemada):
        self.X = propiedad
        self.Y = area_quemada
        media_x = self.media_muestra_x()
        media_y = self.media_muestra_y()
        distancia_x = self.distancia_media_x(media_x)
        distancia_y = self.distancia_media_y(media_y)
        coeficiente_x_y = self.num_coeficiente_x_y(distancia_x,distancia_y)
        denominador_x_y = self.den_coeficiente_x_y(distancia_x,distancia_y)
        self._coeficiente = self.calculo_coeficiente(coeficiente_x_y,denominador_x_y)
    
    @property
    def coeficiente(self):
        return self._coeficiente

    def media_muestra_x(self):
        sumatoria = 0
        for i in self.X:
            sumatoria += i
        self.media_x = sumatoria / len(self.X)
        return self.media_x
    
    def media_muestra_y(self):
        sumatoria = 0
        for i in self.Y:
            sumatoria += i
        self.media_y = sumatoria / len(self.Y)
        return self.media_y

    def distancia_media_x(self, media_x):
        self.dist_x = []
        for i in self.X:
            self.dist_x.append((i - media_x))
        return self.dist_x
        
    def distancia_media_y(self, media_y):
        self.dist_y = []
        for i in self.Y:
            self.dist_y.append((i - media_y))
        return self.dist_y

    def num_coeficiente_x_y(self, distancia_x, distancia_y):
        self.numerador = 0
        for i in range(len(self.X)):
            self.numerador += distancia_x[i]*distancia_y[i]
        return self.numerador
    
    def den_coeficiente_x_y(self,distancia_x, distancia_y):
        cuadrado_x = 0
        cuadrado_y = 0
        
        for i in range(len(self.X)):
            cuadrado_x += pow(distancia_x[i],2)
        for i in range(len(self.Y)):
            cuadrado_y += pow(distancia_y[i],2)
            
        self.denominador = sqrt(cuadrado_x*cuadrado_y)
        return self.denominador
        

    def calculo_coeficiente(self, numerador, denominador):
        return (numerador / denominador)   
    