class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"__str__ method: {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"__repr__ method: {self.first_name} {self.last_name}"


user = User("Vasya", "Pypkin")
print(f"{user}")
print(user)
print(user.__str__())
print(user.__repr__())
print()
# Но если вместо __str__ метода нужно применить метод __repr__ — можно
# воспользоваться либо функцией repr  либо флагом преобразования !r
print(f"{repr(user)}")
# или лучше воспользоваться !r
print(f"{user!r}")
