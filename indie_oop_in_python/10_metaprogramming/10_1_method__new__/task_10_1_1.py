class Circle:
    PI = 3.14

    def __new__(cls, radius):
        cls.get_radius = lambda self: self._radius
        cls.get_diameter = lambda self: self._diameter
        cls.get_area = lambda self: self.PI * self._radius ** 2
        cls.get_perimeter = lambda self: 2 * self.PI * self._radius
        instance = super().__new__(cls)
        instance._radius = radius
        instance._diameter = 2 * radius
        return instance


# Проверка работы кода--------------------------------------------------------
circle_instance = Circle(3.5)

print(f"Radius: {circle_instance.get_radius()}")
print(f"Diameter: {circle_instance.get_diameter()}")
print(f"Area: {circle_instance.get_area()}")
print(f"Perimeter: {circle_instance.get_perimeter()}")
