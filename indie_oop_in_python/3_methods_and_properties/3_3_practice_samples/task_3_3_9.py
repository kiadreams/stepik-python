# Напишите определение класса Triangle
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self):
        checks = [
            (self.a + self.b) > self.c,
            (self.a + self.c) > self.b,
            (self.b + self.c) > self.a,
        ]
        return all(checks)

    def is_equilateral(self):
        return self.a == self.b == self.c

    def is_isosceles(self):
        checks = [
            self.a == self.b,
            self.a == self.c,
            self.c == self.b,
        ]
        return self.is_exists() and any(checks)
