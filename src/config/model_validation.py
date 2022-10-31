from dataclasses import dataclass
from src.enums.day import Day
from src.enums.month import Month

from src.utils.validation import Validation

@dataclass
class ModelValidation:
    @staticmethod
    def coordenada():
        return [
            Validation('x', 1, 9),
            Validation('y', 2, 9)
        ]
    @staticmethod
    def estado():
        return [
            Validation('temperature', -15, 45),
            Validation('humidity', 0, 100),
            Validation('wind', 0.0, 10.0),
            Validation('rain', 0.0, 7.0),
            Validation('surface', 0, 1000)
        ]
    @staticmethod
    def fecha():
        return [
            Validation('mes', enum=Month),
            Validation('dia', enum=Day)
        ]
    @staticmethod
    def fwi():
        return [
            Validation('FFMC', 18.7, 96.0),
            Validation('DMC', 1.1, 290.0),
            Validation('DC', 7.9, 860.0),
            Validation('ISI', 0.0, 56.0)
        ]
