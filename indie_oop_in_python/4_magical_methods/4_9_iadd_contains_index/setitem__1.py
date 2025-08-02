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
        # self.values[key] = value # Как вариант...


v = Vector(10, 9, 8, 7)
print(v)  # Vector(10, 9, 8, 7)
v[1] = 25
v[3] = 16
v[30] = 16
print(v)  # Vector(10, 25, 8, 16)
