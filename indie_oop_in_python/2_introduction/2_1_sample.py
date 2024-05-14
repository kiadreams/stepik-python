class Car:
    pass


a = Car()
b = Car()

print(id(a), a)
print(id(b), b)

print(hasattr(a, 'a'))
print(setattr(a, 'a', 10))
print(a.__dict__, b.__dict__)
print(Car.__dict__)
print(delattr(a, 'a'))
print(a.__dict__)