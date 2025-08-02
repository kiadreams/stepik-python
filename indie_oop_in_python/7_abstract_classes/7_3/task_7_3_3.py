class PowerTwo:

    def __init__(self, power):
        self.power = power
        self.curr_pow = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_pow < self.power:
            self.curr_pow += 1
            return 2**self.curr_pow
        else:
            raise StopIteration


for i in PowerTwo(4):  # итерируемся до 4й степени двойки
    print(i)
