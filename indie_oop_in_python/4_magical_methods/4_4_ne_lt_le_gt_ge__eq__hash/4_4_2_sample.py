from functools import total_ordering


# Декоратор total_ordering позволил реализовать все магические методы
# сравнения для класса Account
@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


acc1 = Account(10)
acc2 = Account(20)
print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
print(acc1 != acc2)
print(acc1 >= acc2)
print(acc1 <= acc2)
