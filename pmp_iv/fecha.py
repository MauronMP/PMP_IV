from dataclasses import dataclass
from enum import Enum
from pmp_iv.model_validation import ModelValidation
from pmp_iv.day import Day
from pmp_iv.month import Month
from pmp_iv.validation import Validation

'''Utilizado para segmentar la información'''
@dataclass
class Fecha:
    '''Opciones posibles para segmentar información mediante meses'''
    mes: Month
    '''Opciones posibles para segmentar información mediante día de la semana'''
    dia: Day

    def __post_init__(self):
        Validation.validate(self, ModelValidation.fecha())

