from pmp_iv.segmentacionCSV.Datos import Datos

def leeCSV():
    datos = Datos()
    return datos.getDF()

def filtrado_Mes():
    muestreoMes = Datos()
    muestreoMes = muestreoMes.filtrar_mes_dia([["month", "==", "'aug'"], ["day", "==", "'mon'"]])
    mes = muestreoMes['month']
    mes.to_dict()
    return mes

def filtrado_Viento():
    filtrado_Mes()
    muestreoMes = Datos()
    mes = muestreoMes.filtrarViento([["month", "==", "'aug'"], ["day", "==", "'mon'"]])
    mes['wind']
    return (list(mes.columns))

def comprobar_Imagen():
    datos = Datos()
    return datos.diagramaDispersion()
