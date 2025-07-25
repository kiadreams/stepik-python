from dataclasses import is_dataclass, dataclass
# Создайте класс данных Point и два экземпляра


@dataclass
class Point:
    x: int
    y: int


point1 = Point(5, 7)
point2 = Point(-10, 12)
я

# Ниже располагается код для проверки

assert is_dataclass(Point), 'Point не dataclass'
assert isinstance(point1, Point)
assert isinstance(point2, Point)
assert point1.x == 5
assert point1.y == 7
assert point2.x == -10
assert point2.y == 12