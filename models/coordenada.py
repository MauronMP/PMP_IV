from dataclasses import dataclass

@dataclass
class Coordenada:
    x: int
    y: int

    def __post_init__(self):
        if self.x < 1 or self.x > 9:
            raise Exception('x property only allows values between 1 and 9')
        if self.y < 2 or self.y > 9:
            raise Exception('x property only allows values between 2 and 9')
