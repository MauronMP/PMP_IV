from dataclasses import dataclass
from enum import Enum

class Months(Enum):
    enero = 1
    febrero = 2
    marzo = 3
    abril = 4
    mayo = 5
    junio = 6
    julio = 7
    agosto = 8
    septiembre = 9
    octubre = 10
    noviembre = 11
    diciembre = 12

class Day(Enum):
    L = 1
    M = 2
    X = 3
    J = 4
    V = 5
    S = 6
    D = 7

@dataclass
class Fecha:
    mes: Months
    dia: Day

    def __post_init__(self):
        if (not isinstance(self.mes, Months)):
            raise Exception('mes property is not Months enum instance')
        if (not isinstance(self.dia, Day)):
            raise Exception('dia property is not Day enum instance')

