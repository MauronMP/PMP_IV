from dataclasses import dataclass

@dataclass
class FWI:
    FFMC: float
    DMC: float
    DC: float
    ISI: float

    def __post_init__(self):
        if self.FFMC < 18.7 or self.FFMC > 96:
            raise Exception('FFMC property only allows values between 18.7 and 96')
        if self.DMC < 1.1 or self.DMC > 290:
            raise Exception('DMC property only allows values between 1.1 and 290')
        if self.DC < 7.9 or self.DC > 860:
            raise Exception('DC property only allows values between 7.9 and 860')
        if self.ISI < 0.0 or self.ISI > 56:
            raise Exception('ISI property only allows values between 0.0 and 56')
