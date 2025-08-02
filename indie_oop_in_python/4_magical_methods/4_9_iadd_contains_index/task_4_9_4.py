class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

    def __delitem__(self, key):
        if key in self.values:
            self.values = [item for item in self.values if item != key]
        else:
            raise ValueError(f'Значение {key} отсутствует в векторе')


# Проверка работы кода--------------------------------------------------------
v1 = Vector(5, 5, 5, 4, 4, 3)
print(v1)
del v1[4]
print(v1)
del v1[5]
print(v1)
try:
    del v1[10]
except ValueError as e:
    print(e)
