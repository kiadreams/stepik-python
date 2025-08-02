from functools import total_ordering


@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, (int, BankAccount)):
            other = other if isinstance(other, int) else other.balance
        return self.balance == other

    def __lt__(self, other):
        if isinstance(other, (int, BankAccount)):
            other = other if isinstance(other, int) else other.balance
        return self.balance < other


if __name__ == "__main__":
    values = [
        BankAccount("Petrovich", 400),
        500,
        BankAccount("Andrey", 200),
        100,
        BankAccount("Zina", 150),
    ]
    values.sort()
    print(*values)
