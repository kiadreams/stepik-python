class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.balance + other

    def __radd__(self, other):
        return self.__add__(other)


class Numbers:
    def __init__(self, values: list):
        self._values = values

    def __add__(self, other):
        return sum(self._values) + other

    def __radd__(self, other):
        return self.__add__(other)


if __name__ == "__main__":
    lst = [500, BankAccount("Vanya", 200), 7, BankAccount("Ivan", 300), 3]
    print(sum(lst))
