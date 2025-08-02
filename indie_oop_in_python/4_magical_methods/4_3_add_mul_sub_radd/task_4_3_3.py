class Vector:

    def __init__(self, *args):
        self.values = sorted(
            [
                arg
                for arg in args
                if isinstance(arg, int) and not isinstance(arg, bool)
            ]
        )

    def __str__(self):
        if self.values:
            all_args = ", ".join(map(str, self.values))
            return f"Вектор({all_args})"
        return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[elem + other for elem in self.values])
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(
                    *[sum(pair) for pair in zip(self.values, other.values)],
                )
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[other * elem for elem in self.values])
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(
                    *[e1 * e2 for e1, e2 in zip(self.values, other.values)]
                )
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    print(v1)  # печатает "Вектор(1, 2, 3)"

    v2 = Vector(3, 4, 5)
    print(v2)  # печатает "Вектор(3, 4, 5)"
    v3 = v1 + v2
    print(v3)  # печатает "Вектор(4, 6, 8)"
    v4 = v3 + 5
    print(v4)  # печатает "Вектор(9, 11, 13)"
    v5 = v1 * 2
    print(v5)  # печатает "Вектор(2, 4, 6)"
    v5 + "hi"  # печатает "Вектор нельзя сложить с hi"
