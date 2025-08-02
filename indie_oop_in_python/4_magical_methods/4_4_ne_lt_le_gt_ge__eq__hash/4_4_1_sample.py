# __eq__(self, other)   сравнение на равенство с помощью оператора ==
# __ne__(self, other)   сравнение на неравенство с помощью оператора !=
# __lt__(self, other)   сравнение на меньше с помощью оператора <
# __le__(self, other)   сравнение на меньше или равно с помощью оператора <=
# __gt__(self, other)   сравнение на больше с помощью оператора >
# __ge__(self, other)   сравнение на больше или равно с помощью оператора >=
print(hash("asd"))
print("asd".__hash__())
print()


class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x is other.x


a = MyClass([1, 2, 3])
b = MyClass([1, 2, 3])
print(id(a.x), id(b.x))
print(id(a.x[0]), id(b.x[0]))
print(a == b)
