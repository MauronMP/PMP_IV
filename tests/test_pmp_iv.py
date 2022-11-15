import os
import pmp_iv.utils.validation 
import pmp_iv.models.fecha 
import pmp_iv.models.estado 
import pmp_iv.models.fwi 
import pmp_iv.enums.day 
import pmp_iv.enums.month
import pmp_iv.models.coordenada
from pmp_iv.forest_prediction.eda import *
from pmp_iv.forest_prediction.model_building import *
import pmp_iv.enums.regression_algorithm
from hamcrest import *

def test_syntaxis():
    os.system("python3 -m compileall pmp_iv")

def test_Constructores():
    assert_that(pmp_iv.models.coordenada.Coordenada(5,5), equal_to(pmp_iv.models.coordenada.Coordenada(5,5)))
    assert_that(pmp_iv.models.coordenada.Coordenada(5,5).x,less_than_or_equal_to(9))
    assert_that(pmp_iv.models.fecha.Fecha(pmp_iv.enums.month.Month.julio,pmp_iv.enums.day.Day.L).mes,same_instance(pmp_iv.enums.month.Month.julio))
    assert_that(pmp_iv.models.estado.Estado(10,10,9,3,200).temperature, less_than_or_equal_to(50))

def test_month_filter():
    filtrado_mes = EDA().by_date_property('aug','mon')
    for i in range(len(filtrado_mes)):
        assert_that(filtrado_mes[i],has_items('aug','mon'))

def test_wind_filter():
    filtrado_mes_viento = EDA().by_date_property('aug','mon','wind')
    for i in range(len(filtrado_mes_viento)):
        assert_that(float(filtrado_mes_viento[i][4]),less_than_or_equal_to(10) and greater_than(0))

def test_regression_selected():
    assert_that(model_building().get_best_results(),anything(Regression_algorithm._member_names_))