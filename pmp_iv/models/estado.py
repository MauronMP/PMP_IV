from dataclasses import dataclass
from pmp_iv.config.model_validation import ModelValidation

from pmp_iv.utils.validation import Validation

@dataclass
class Estado:
    temperature: int
    humidity: int
    wind: float
    rain: float
    surface: int

    def __post_init__(self):
        Validation.validate(self, ModelValidation.estado())
