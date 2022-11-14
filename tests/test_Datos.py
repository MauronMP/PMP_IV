from hamcrest import *
from pmp_iv.segmentacionCSV.Datos import *
import os

def test_sizeOf_CSV():
    assert_that(Datos().size_of_CSV(), equal_to(517))

def test_month_filter():
    filtrado_mes = Datos().by_date_property('aug','mon')
    for i in range(len(filtrado_mes)):
        assert_that(filtrado_mes[i],has_items('aug','mon'))

def test_wind_filter():
    filtrado_mes_viento = Datos().by_date_property('aug','mon','wind')
    for i in range(len(filtrado_mes_viento)):
        assert_that(float(filtrado_mes_viento[i][4]),less_than_or_equal_to(10) and greater_than(0))

def test_create_image():
    filtrado_mes_viento = Datos().by_date_property('aug','mon','wind')
    filtrado_mes_area = Datos().by_date_property('aug','mon','area')
    imagen_creada = Datos().diagramaDispersion(filtrado_mes_viento,filtrado_mes_area, 'Viento')
    os.system("find output/diagramaDispersion -name {imagen_creada} ")
