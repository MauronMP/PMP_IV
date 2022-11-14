import csv
import math
import matplotlib.pyplot as plt
class Datos():
    
    def size_of_CSV(self):
        with open('data/incendiosForestales.csv', 'r', newline='') as file:
            content = file.readlines()
        rows = content[1:]
        return len(rows)

    def by_date_property(self, mes, dia, propiedad=None):
        mes_dia = []
        with open('data/incendiosForestales.csv', 'r', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                if(row['month'] == mes and row['day'] == dia and propiedad is not None):
                    mes_dia.append( [row['X'], row['Y'],row['month'], row['day'],row[propiedad]])
                elif(propiedad is None and row['month'] == mes and row['day'] == dia):
                    mes_dia.append( [row['X'], row['Y'],row['month'], row['day']])
        return mes_dia
    
    def only_one_column(self, data, column):
        filter_column = []
        for i in range(len(data)):
            filter_column.append(data[i][column])
        return filter_column
    
    def diagramaDispersion(self,data,area,image_name):
        area_filter = self.only_one_column(area,4)
        for i in range(len(area_filter)):
            area_filter[i] = (math.log10(((float(area[i][4]))+1)))
        plt.xlabel("Area")
        plt.scatter(self.only_one_column(data,4),area_filter)
        plt.title("Diagrama dispersión")
        plt.savefig('output/diagramaDispersion/'+image_name+'.png',dpi=200)
        return image_name+'.png'