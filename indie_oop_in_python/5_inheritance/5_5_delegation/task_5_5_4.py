# Напишите определение классов Vehicle Bus и Taxi
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f"Total {self.name} fare is: {self.fare()}")


class Bus(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, 50)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, 4)

    def fare(self):
        return super().fare() * 1.35


# Ниже располагается код для проверки
sc = Vehicle("Scooter", 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()

t = Taxi("x", 111)
assert t.__dict__ == {"name": "x", "mileage": 111, "capacity": 4}
t.display()
b = Bus("t", 123)
assert b.__dict__ == {"name": "t", "mileage": 123, "capacity": 50}
b.display()
