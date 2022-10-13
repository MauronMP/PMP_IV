from dataclasses import dataclass
from pmp_iv.config.model_validation import ModelValidation

from pmp_iv.utils.validation import Validation

@dataclass
class FWI:
    FFMC: float
    DMC: float
    DC: float
    ISI: float

    def __post_init__(self):
        Validation.validate(self, ModelValidation.fwi())
