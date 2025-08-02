class RangeValidator:

    def __init__(self, start: int | float, end: int | float) -> None:
        self.start = start
        self.end = end

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        if value < self.start or value > self.end:
            raise ValueError(
                f'Значение должно быть между {self.start} и {self.end}'
            )
        instance.__dict__[self.start] = value


# Проба работы----------------------------------------------------------------
class Temperature:
    celsius = RangeValidator(-273.15, 1000)


temp = Temperature()
try:
    temp.celsius = [1, 2]
except TypeError as ex:
    print(ex)


class Temperature:
    celsius = RangeValidator(-273.15, 1000)


temp = Temperature()
try:
    temp.celsius = -300
except ValueError as ex:
    print(ex)
