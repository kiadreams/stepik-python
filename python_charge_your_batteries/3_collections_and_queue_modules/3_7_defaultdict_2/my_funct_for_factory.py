from collections import defaultdict


# Передача своей функции
def get_value():
    return 'DEFAULT'


dd_1 = defaultdict(get_value)
dd_1['a']
dd_1['b'] += '!!!'
dd_1[10].upper()
print(dd_1)
print()

dd_2 = defaultdict(lambda: 100)
dd_2['a']
dd_2['b']
dd_2[10] += 15
print(dd_2)
print()


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = []

    def __repr__(self):
        return f"Student {self.first_name} {self.last_name} {self.marks}"


def create_student(first_name, last_name):
    return Student(first_name, last_name)


dd_3 = defaultdict(lambda: create_student("John", "Doe"))

dd_3[1]
dd_3['a'].marks += [4, 5]
dd_3['a'].first_name = 'Ben'
dd_3[3] = create_student("Jane", "Smith")
print(dd_3)
