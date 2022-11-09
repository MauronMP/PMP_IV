#!/usr/bin/env python
# coding: utf-8

# In[6]:

import os
import pytest
from testbook import testbook
from hamcrest import *


@pytest.fixture(scope='module')
def tb():
    with testbook('/home/mauron/Dropbox/UGR/IV/notebooks/Tests.ipynb', execute=True) as tb:
        yield tb

def test_tamanio_CSV(tb):
    leeCSV = tb.ref("leeCSV")
    assert_that(len(leeCSV()), equal_to(517))

def test_filtrado_Mes(tb):
    filtrado_Mes = tb.ref("filtrado_Mes")
    assert_that(filtrado_Mes(),has_item('aug'))

def test_filtrado_Viento(tb):
    filtrado_Viento = tb.ref("filtrado_Viento")
    assert_that(filtrado_Viento(),has_item('wind'))

def test_comprobar_Imagen(tb):
    comprobar_Imagen = tb.ref("comprobar_Imagen")
    num_imagenes = os.system("ls -lR /home/mauron/Dropbox/UGR/IV/output/diagramaDispersion/*.png | wc -l")
    assert_that(comprobar_Imagen(),equal_to(10))

# In[ ]:




