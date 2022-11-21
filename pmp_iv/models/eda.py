import csv
from pmp_iv.models.correlacion_area import *
class EDA():

    def __init__(self):      
        with open('data/incendiosForestales.csv', 'r', newline='') as csvfile:       
            self.weather_data = csv.DictReader(csvfile)
            self._datos_csv = self.get_data_values()
            self._area = self.by_property('area')
 
    def get_data_values(self):
        filter_data = []
        for row in self.weather_data:
            my_dict = {}
            for key, value in row.items():
                if key != 'month' and key != 'day':
                    my_dict[key] = float(value)
                else:
                    my_dict[key] = value
            filter_data.append(my_dict)
        return filter_data
    
    def by_date_property(self, mes, dia, propiedad):
        data_by_property = []
        for i in self.valores:
            if i['month']==mes and i['day']==dia:
                data_by_property.append([i['X'], i['Y'],i['month'], i['day'], i[propiedad]])
        return data_by_property

    
    def by_property(self,propiedad):
        data_by_property = [i[propiedad] for i in self.valores] 
        return data_by_property
    
    def weather_values(self):
        data_by_value = [[i['FFMC'],i['DMC'],i['DC'],i['ISI'],
                     i['temp'],i['RH'],i['wind'],i['area']] for i in self.valores] 
        return data_by_value
      
    @property
    def valores(self):
        return self._datos_csv
    
    @property
    def area(self):
        return self._area