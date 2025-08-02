class Person:

    def breath(self):
        print("Человек дышит")

    def sleep(self):
        print("Человек спит")

    def combo(self):
        self.breath()
        if hasattr(self, "walk"):
            self.walk()
        self.sleep()
        if hasattr(self, "age"):
            print(self.age)


class Doctor(Person):
    age = 20

    def breath(self):
        print("ДОКТОР дышит")

    def walk(self):
        print("ДОКТОР идет")


a = Doctor()
a.combo()

print("-------")
b = Person()
b.combo()
