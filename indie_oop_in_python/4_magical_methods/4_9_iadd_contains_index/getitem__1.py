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


v1 = Vector(3, 655, 323, 672, 11, 6)
print(v1[2])  # 323
print(v1[0])  # 3
print(v1[5])  # 6
try:
    print(v1[10])
except IndexError as e:
    print(e)
