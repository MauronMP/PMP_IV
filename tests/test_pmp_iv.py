import pmp_iv.utils.validation 
import pmp_iv.models.fecha 
import pmp_iv.models.estado 
import pmp_iv.models.fwi 
import pmp_iv.enums.day 
import pmp_iv.enums.month
import pmp_iv.models.coordenada

def test():
    assert pmp_iv.models.coordenada.Coordenada(5,5)
    assert pmp_iv.models.fecha.Fecha(pmp_iv.enums.month.Month.julio,pmp_iv.enums.day.Day.L)
    assert pmp_iv.models.estado.Estado(10,10,9,3,200)
    assert pmp_iv.models.fwi.FWI(30.4,124.5,664.9,32.6)
