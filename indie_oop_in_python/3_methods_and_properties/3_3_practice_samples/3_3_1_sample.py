class Car:
    list_car = []

    def __init__(self, make, model):
        self.make = make
        self.maker = model
        self.list_car.append(self)

    def display_info(self):
        return f"{self.make} {self.maker}"


car = Car("Toyota", "Camry")
print(car.display_info())
print(car.__dict__, car)
print(Car.__dict__)
