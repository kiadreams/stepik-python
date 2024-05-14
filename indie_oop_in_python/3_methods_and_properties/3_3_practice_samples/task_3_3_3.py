class Numbers:

    def __init__(self, *args):
        self.numbers = list(args)

    def add_number(self, number):
        self.numbers.append(number)

    def get_positive(self):
        return [number for number in self.numbers if number > 0]

    def get_negative(self):
        return [number for number in self.numbers if number < 0]

    def get_zeroes(self):
        return [number for number in self.numbers if number == 0]
