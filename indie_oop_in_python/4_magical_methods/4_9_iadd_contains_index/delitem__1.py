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

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError(f"Индекс {key} находится за пределами вектора")

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError(f"Индекс {key} находится за пределами вектора")


v = Vector(10, 9, 12, 7, 14)
print(v)  # Vector(10, 9, 12, 7, 14)
del v[1]  # удаляем индекс 1 из .values.  После этого индексы элементов сместятся
print(v)  # Vector(10, 12, 7, 14)
del v[2]
print(v)  # Vector(10, 12, 14)
