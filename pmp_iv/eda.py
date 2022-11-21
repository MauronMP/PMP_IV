import csv
from operator import itemgetter

class EDA():

    def __init__(self):      
        with open('data/incendiosForestales.csv', 'r', newline='') as csvfile:       
            self.weather_data = csv.DictReader(csvfile)
            self._datos_csv = self.get_data_values()
            self._area = self.by_property('area')
 
    def get_data_values(self):
        data = []
        for row in self.weather_data:
            d = {}
            for key, value in row.items():
                if key != 'month' and key != 'day':
                    d[key] = float(value)
                else:
                    d[key] = value
            data.append(d)
        return data
    
    def by_date_property(self, mes, dia, propiedad):
        propiedad_fecha = list(map(itemgetter('X', 'Y', 'month','day',propiedad), self.valores))
        return propiedad_fecha

    def by_property(self,propiedad):
        filtrado_propiedad = list(map(itemgetter(propiedad), self.valores))
        return filtrado_propiedad
    
    def weather_values(self):
        valores_clima = list(map(itemgetter('FFMC', 'DMC', 'DC','ISI', 'temp', 'RH', 'wind', 'area'), self.valores))
        return valores_clima
      
    @property
    def valores(self):
        return self._datos_csv
    
    @property
    def area(self):
        return self._area