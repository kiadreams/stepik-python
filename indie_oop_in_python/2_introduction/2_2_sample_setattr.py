class Empty:
    pass


my_list = [
    ("apple", 23),
    ("banana", 80),
    ("cherry", 13),
    ("date", 10),
    ("elderberry", 4),
    ("fig", 65),
    ("grape", 5),
    ("honeydew", 7),
    ("kiwi", 1),
    ("lemon", 10),
]

a = Empty()
print(Empty.__dict__)
print(a.__dict__)
print()

for attribute, some_value in my_list:
    setattr(Empty, attribute, some_value)

a = Empty()
print(Empty.__dict__)
print(a.apple)

