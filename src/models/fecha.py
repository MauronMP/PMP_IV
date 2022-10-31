from dataclasses import dataclass
from enum import Enum
from src.config.model_validation import ModelValidation
from src.enums.day import Day
from src.enums.month import Month
from src.utils.validation import Validation

'''Utilizado para segmentar la información'''
@dataclass
class Fecha:
    '''Opciones posibles para segmentar información mediante meses'''
    mes: Month
    '''Opciones posibles para segmentar información mediante día de la semana'''
    dia: Day

    def __post_init__(self):
        Validation.validate(self, ModelValidation.fecha())

