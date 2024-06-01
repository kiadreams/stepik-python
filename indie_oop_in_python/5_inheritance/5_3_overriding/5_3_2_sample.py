class CURD:
    def __init__(self):
        C().create()
        R().read()
        U().update()
        D().delete()


class C:
    def create(self):
        print("c", end="")


class U:
    def update(self):
        print("u", end="")


class R(C):
    def create(self):
        print("C", end="")

    def read(self):
        print("R", end="")


class D(U):
    def update(self):
        print("U", end="")

    def delete(self):
        print("D", end="")


CURD()

print("\n")


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"


class Doctor(Person):
    pass


p = Person("Vasia")
d = Doctor("Petia")
print(p, d, sep="\n")
