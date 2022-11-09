import os
import pmp_iv.utils.validation 
import pmp_iv.models.fecha 
import pmp_iv.models.estado 
import pmp_iv.models.fwi 
import pmp_iv.enums.day 
import pmp_iv.enums.month
import pmp_iv.models.coordenada

from hamcrest import *

def test_syntaxis():
    os.system("python3 -m compileall pmp_iv")

def test_Constructores():
    assert_that(pmp_iv.models.coordenada.Coordenada(5,5), equal_to(pmp_iv.models.coordenada.Coordenada(5,5)))
    assert_that(pmp_iv.models.coordenada.Coordenada(5,5).x,less_than_or_equal_to(9))
    assert_that(pmp_iv.models.fecha.Fecha(pmp_iv.enums.month.Month.julio,pmp_iv.enums.day.Day.L).mes,same_instance(pmp_iv.enums.month.Month.julio))
    assert_that(pmp_iv.models.estado.Estado(10,10,9,3,200).temperature, less_than_or_equal_to(50))



