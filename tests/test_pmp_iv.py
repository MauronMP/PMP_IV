import os
import pmp_iv.utils.validation 
import pmp_iv.models.fecha 
import pmp_iv.models.estado 
import pmp_iv.models.fwi 
import pmp_iv.enums.day 
import pmp_iv.enums.month
import pmp_iv.models.coordenada
from pmp_iv.forest_prediction.eda import *
from pmp_iv.forest_prediction.correlacion_area import *
from hamcrest import *

MES_AGOSTO = 'aug'
DIA_LUNES = 'mon'
PROPIEDAD_VIENTO = 'wind'
MIN_VIENTO = 0
MAX_VIENTO = 10
MIN_CORRELACION = -1
MAX_CORRELACION = 1
MAXIMA_TEMPERATURA = 50
MAXIMA_COORDENADA = 9

def test_syntaxis():
    os.system("python3 -m compileall pmp_iv")

def test_Constructores():
    assert_that(pmp_iv.models.coordenada.Coordenada(5,5).x,less_than_or_equal_to(MAXIMA_COORDENADA))
    assert_that(pmp_iv.models.fecha.Fecha(pmp_iv.enums.month.Month.julio,pmp_iv.enums.day.Day.L).mes,same_instance(pmp_iv.enums.month.Month.julio))
    assert_that(pmp_iv.models.estado.Estado(10,10,9,3,200).temperature, less_than_or_equal_to(MAXIMA_TEMPERATURA))

def test_month_filter():
    filtrado_mes = EDA().by_date_property(MES_AGOSTO,DIA_LUNES)
    for i in range(len(filtrado_mes)):
        assert_that(filtrado_mes[i],has_items(MES_AGOSTO,DIA_LUNES))

def test_wind_filter():
    filtrado_mes_viento = EDA().by_date_property(MES_AGOSTO,DIA_LUNES,PROPIEDAD_VIENTO)
    for i in range(len(filtrado_mes_viento)):
        assert_that(float(filtrado_mes_viento[i][4]),less_than_or_equal_to(MAX_VIENTO) and greater_than(MIN_VIENTO))

def test_correlacion():
    assert_that(correlacion_dato_area(PROPIEDAD_VIENTO).calculo_coeficiente(), less_than_or_equal_to(MAXIMA_COORDENADA))
    assert_that(correlacion_dato_area(PROPIEDAD_VIENTO).calculo_coeficiente(), greater_than_or_equal_to(MIN_CORRELACION))