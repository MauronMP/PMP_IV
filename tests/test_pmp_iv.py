from pmp_iv.utils.validation import *
from pmp_iv.models.coordenada import *
from pmp_iv.models.fecha import *
from pmp_iv.models.estado import *
from pmp_iv.models.fwi import *
from pmp_iv.enums.day import *
from pmp_iv.enums.month import *

def test():
    assert Coordenada(5,5)
    assert Fecha(Month.julio,Day.L)
    assert Estado(10,10,9,3,200)
    assert FWI(30.4,124.5,664.9,32.6)
