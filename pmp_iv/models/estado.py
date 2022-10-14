from dataclasses import dataclass
from pmp_iv.config.model_validation import ModelValidation

from pmp_iv.utils.validation import Validation

'''Propiedades últiles para poder realizar el cálculo de los elementos de la clase fwi'''
@dataclass
class Estado:
    '''Temperatura en la coordenada'''
    temperature: int
    '''Humedad en la coordenada'''
    humidity: int
    '''Densidad del viento en la coordenada'''
    wind: float
    '''Cantidad de lluvia en la coordenada'''
    rain: float
    '''Superficie de la coordenada'''
    surface: int

    def __post_init__(self):
        Validation.validate(self, ModelValidation.estado())
