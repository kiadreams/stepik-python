from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, width):
        self.width = width

    @abstractmethod
    def area(self) -> int:
        return self.width**2

    @abstractmethod
    def perimetr(self) -> int: ...


class Square(Shape):

    def area(self):
        return super().area()

    def perimetr(self):
        return self.width * 4


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return (self.width + self.height) * 2


some_list = [
    Square(5),
    Square(7),
    Square(45),
    Rectangle(45, 6),
    Rectangle(3, 4),
]
for elem in some_list:
    print(elem.__class__)
    print(elem.area())
    print(elem.perimetr())
    print()
