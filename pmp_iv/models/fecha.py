from dataclasses import dataclass
from enum import Enum
from pmp_iv.config.model_validation import ModelValidation
from pmp_iv.enums.day import Day
from pmp_iv.enums.month import Month
from pmp_iv.utils.validation import Validation


@dataclass
class Fecha:
    mes: Month
    dia: Day

    def __post_init__(self):
        Validation.validate(self, ModelValidation.fecha())

