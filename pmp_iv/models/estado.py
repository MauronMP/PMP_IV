from dataclasses import dataclass

@dataclass
class Estado:
    temperature: int
    humidity: int
    wind: float
    rain: float
    surface: int

    def __post_init__(self):
        if self.temperature < -15 or self.temperature > 45:
            raise Exception('temperature property only allows values between -15 and 45')
        if self.humidity < 0 or self.humidity > 100:
            raise Exception('humidity property only allows values between 0 and 100')
        if self.wind < 0.0 or self.wind > 10:
            raise Exception('wind property only allows values between 0 and 10')
        if self.rain < 0.0 or self.rain > 7:
            raise Exception('rain property only allows values between 0.0 and 7')
        if self.surface < 0 or self.surface > 1000:
            raise Exception('surface property only allows values between 0 and 1000')
