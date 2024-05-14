class Car:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Car.", args, kwargs)
        return super().__new__(cls)

    def __init__(self, new_model, new_engine, new_horse_power):
        print("2. Initialize the new instance of Car.")
        self.model = new_model
        self.engine = new_engine
        self.horse_power = new_horse_power


# вызывается метод __init__
bmw_3 = Car("BMW", 3, 500)
print(bmw_3.__dict__)
