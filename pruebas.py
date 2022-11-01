from os import fwalk
from src.utils.validation import *
from src.models.coordenada import *
from src.models.fecha import *
from src.models.estado import *
from src.models.fwi import *
from src.enums.day import *
from src.enums.month import *


def testeo():
    coordenada_1 = Coordenada(2,9)
    fecha = Fecha(Month.julio,Day.L)
    estado = Estado(10,10,9,3,200)
    fwi = FWI(30.4,124.5,664.9,32.6)

    print(coordenada_1)
    print(fecha)
    print(estado)
    print(fwi)

