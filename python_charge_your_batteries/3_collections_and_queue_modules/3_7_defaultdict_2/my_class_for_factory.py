from collections import defaultdict


# Передача своего класса
class MyClass:
    def __init__(self):
        self.count = 0

    def __repr__(self):
        return f'MyCount({self.count})'


dct = defaultdict(MyClass)

dct['a'].count += 1
dct['b'].count += 2

print(dct)
print()
