import os
import pytest
from pmp_iv.eda import *
from pmp_iv.correlacion_area import *
from hamcrest import *


MES_AGOSTO = 'aug'
DIA_LUNES = 'mon'
PROPIEDAD_VIENTO = 'wind'
MIN_VIENTO = 0
MAX_VIENTO = 10
MIN_CORRELACION = -1
MAX_CORRELACION = 1
POS_VIENTO = 4

#Arrange
@pytest.fixture
def get_eda():
    eda = EDA()
    return eda

@pytest.fixture
def get_correlacion(get_eda):
    correlacion = correlacion_area(get_eda.area, get_eda.by_property(PROPIEDAD_VIENTO))
    return correlacion

def test_wind_filter(get_eda):
    #Act
    filtrado_viendo = get_eda.by_date_property(MES_AGOSTO,DIA_LUNES,PROPIEDAD_VIENTO)

    #Assert
    for i in range(len(filtrado_viendo)):
        assert_that(float(filtrado_viendo[i][POS_VIENTO]),less_than_or_equal_to(MAX_VIENTO) and greater_than(MIN_VIENTO))

def test_correlacion(get_correlacion):
    #Act
    calc_correlacion = get_correlacion.coeficiente

    #Assert
    assert_that(calc_correlacion, less_than_or_equal_to(MAX_CORRELACION))
    assert_that(calc_correlacion, greater_than_or_equal_to(MIN_CORRELACION))
    