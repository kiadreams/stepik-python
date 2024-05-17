# Напишите определение класса Celsius
class Celsius:

    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273.15:
            raise ValueError("Неправильное значение температуры...")
        else:
            self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 9 / 5) + 32


# Ниже код для проверки методов класса Celsius

celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0
print("Good")
