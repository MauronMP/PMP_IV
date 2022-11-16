from pmp_iv.forest_prediction.eda import *
from math import *

class correlacion_dato_area():
    
    def __init__(self, propiedad):
        self.X = EDA().by_property(propiedad)
        self.Y = EDA().by_property('area')
    
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

    def distancia_media_x(self):
        self.dist_x = []
        for i in self.X:
            self.dist_x.append((i - self.media_muestra_x()))
        return self.dist_x
        
    def distancia_media_y(self):
        self.dist_y = []
        for i in self.Y:
            self.dist_y.append((i - self.media_muestra_y()))
        return self.dist_y

    def num_coeficiente_x_y(self):
        self.numerador = 0
        for i in range(len(self.X)):
            self.numerador += self.distancia_media_x()[i]*self.distancia_media_y()[i]
        return self.numerador
    
    def den_coeficiente_x_y(self):
        cuadrado_x = 0
        cuadrado_y = 0
        
        for i in range(len(self.X)):
            cuadrado_x += pow(self.distancia_media_x()[i],2)
        for i in range(len(self.Y)):
            cuadrado_y += pow(self.distancia_media_y()[i],2)
            
        self.denominador = sqrt(cuadrado_x*cuadrado_y)
        return self.denominador
        

    def calculo_coeficiente(self):
        return (self.num_coeficiente_x_y() / self.den_coeficiente_x_y())   