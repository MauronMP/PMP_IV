from dataclasses import dataclass
from enum import Enum
from typing import Optional

@dataclass
class Validation:
    prop_name: str
    min: Optional[float] = None
    max: Optional[float] = None
    enum: Optional[Enum] = None

    def __post_init__(self):
        if not self.prop_name or len(self.prop_name) == 0:
            raise Exception('validation must refer to a property name')
        if self.enum and not issubclass(self.enum, Enum):
            raise Exception('if set, enum property must be of type Enum')

    @staticmethod
    def validate(target, validators):
        if (not hasattr(validators, "__len__") and isinstance(validators, Validation)):
            validators = [validators]

        if (not hasattr(validators, "__len__")):
            raise Exception("validators is not Validation or Validation array instance".format())

        i=0
        for validator in validators:
            i+=1
            # Validator checks
            if (not isinstance(validator, Validation)):
                raise Exception("validator {} is not validation instance".format(i))
            if (not hasattr(target, validator.prop_name)):
                raise Exception("to validate property {} it must exists at target object".format(validator.prop_name))
            # Target instance checks
            if (validator.min != None and getattr(target, validator.prop_name) < validator.min):
                raise Exception("{} property only allows greater or equal than {}".format(validator.prop_name, validator.min))
            if (validator.max != None and getattr(target, validator.prop_name) > validator.max):
                raise Exception("{} property only allows lower or equal than {}".format(validator.prop_name, validator.max))
            if (validator.enum != None and not isinstance(getattr(target, validator.prop_name), validator.enum)):
                raise Exception("{} property must be of type {}".format(validator.prop_name, validator.enum))

