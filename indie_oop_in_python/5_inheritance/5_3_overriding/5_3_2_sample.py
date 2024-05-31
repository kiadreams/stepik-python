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
