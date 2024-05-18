# Напишите определение класса Rectangle
class Rectangle:

    def __init__(self, width, length):
        self. width = width
        self.length = length

    @property
    def area(self):
        return self.length * self.width

# Ниже код для проверки методов класса Rectangle


r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')