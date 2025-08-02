# Если нужно, чтобы отработал .__init__() у всех родителей, то необходимо для
# второго родителя напрямую прописать вызова метода .__init__().

class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def can_cure(self):
        print('Я доктор, я умею лечить')


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def can_build(self):
        print('Я строитель, я умею строить')


class Person(Builder, Doctor, ):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def can_build(self):
        print('Я человек, я тоже умею строить')

    def __str__(self):
        return f'Person {self.rank} {self.degree}'


print(Person.__mro__)
s = Person(5, 'spec')
print(s)
