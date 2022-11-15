import csv

class EDA():
    
    def __init__(self):      
        csvfile = open('data/incendiosForestales.csv', 'r', newline='')
        self.weather_data = csv.DictReader(csvfile)
        
    def by_date_property(self, mes, dia, propiedad=None):
        mes_dia = []
        for row in self.weather_data:
            if(row['month'] == mes and row['day'] == dia and propiedad is not None):
                mes_dia.append( [row['X'], row['Y'],row['month'], row['day'],row[propiedad]])
            elif(propiedad is None and row['month'] == mes and row['day'] == dia):
                mes_dia.append( [row['X'], row['Y'],row['month'], row['day']])
        return mes_dia
    
    def by_property(self,propiedad):
        list_property = []
        for row in self.weather_data:
            list_property.append(row[propiedad])
        list_property = [float(i) for i in list_property]
        return list_property
    
    def weather(self):
        all_propierties = []
        for row in self.weather_data:
            all_propierties.append([row['FFMC'], row['DMC'], row['DC'], row['ISI'],
                                    row['temp'], row['RH'],row['wind'], row['area']])
        all_propierties = [list(map(float, sublist)) for sublist in all_propierties]
        return all_propierties