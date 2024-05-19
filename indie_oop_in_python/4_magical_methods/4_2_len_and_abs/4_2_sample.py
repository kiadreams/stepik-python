class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Главное чтобы метод __len__ возвращал целое число не меньше нуля.
    # Иначе вы будет получать ошибки
    # def __len__(self):
    #     return -3
    def __len__(self):
        return len(self.first_name + self.last_name)


class Distance:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        print("Call __len__")
        return abs(self)

    def __abs__(self):
        print("Call __abs__")
        return abs(self.point1 - self.point2)


d = Distance(5, 9)
print(len(d))

d_2 = Distance(8, 3)
print(len(d_2))

john = Person("John", "Doe")
print(len(john))
