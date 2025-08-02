class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Хирург")
        print("---Ищи, начиная с Доктора---")
        super(Doctor, self).tell_about_yourself()
        print("Я Хирург")


s = Surgeon()
s.tell_about_yourself()