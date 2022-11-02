from dataclasses import dataclass
from pmp_iv.config.model_validation import ModelValidation
from pmp_iv.utils.validation import Validation

'''Establece en un perímetro una zona delimitada una área'''
@dataclass
class Coordenada:
    '''Primera coordenada de un cuadrado 3x3'''
    x: int
    '''Segunda coordenada de un cuadrado 3x3'''
    y: int

    def __post_init__(self):
        Validation.validate(self, ModelValidation.coordenada())
