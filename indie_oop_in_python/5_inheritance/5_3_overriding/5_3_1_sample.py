class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I'm person {self.name}"

    def breath(self):
        print("Человек дышит")

    def walk(self):
        print("Человек ходит")

    def sleep(self):
        print("Человек спит")

    def combo(self):
        self.breath()
        self.walk()
        self.sleep()


class Doctor(Person):
    def __str__(self):
        return f"I'm doctor {self.name}"

    def breath(self):
        print("ДОКТОР дышит")


a = Doctor("John")
a.combo()

print("-------")
b = Person("Mike")
b.combo()
