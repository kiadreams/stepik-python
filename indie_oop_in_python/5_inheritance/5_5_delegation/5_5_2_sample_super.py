class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    # def tell_about_yourself(self):
    #     super().tell_about_yourself()
    #     print("Я Доктор")
    pass


class Surgeon(Doctor):
    def tell_about_yourself(self):
        super().tell_about_yourself()
        print("Я Хирург")


s = Surgeon()
s.tell_about_yourself()
print()
