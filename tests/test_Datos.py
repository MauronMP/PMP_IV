from hamcrest import *
from pmp_iv.segmentacionCSV.Datos import *
from pmp_iv.segmentacionCSV.Tests import *

def test_tamanio_CSV():
    assert_that(len(leeCSV()), equal_to(517))

def test_filtrado_Mes():
    assert_that(filtrado_Mes(),has_item('aug'))

def test_filtrado_Viento():
    assert_that(filtrado_Viento(),has_item('wind'))

def test_comprobar_Imagen():
    assert_that(comprobar_Imagen(),equal_to(4))
