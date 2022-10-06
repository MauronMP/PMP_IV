from models.fwi import FWI
from models.fecha import Fecha,Months,Day
from models.coordenada import Coordenada

fwi_instance = FWI(34.4, 44.4, 17.7, 14.3)
print(fwi_instance)

fecha_instance = Fecha(Months.enero, Day.M)
print(fecha_instance)

coordenada_instance = Coordenada(3, 4)
print(coordenada_instance)
