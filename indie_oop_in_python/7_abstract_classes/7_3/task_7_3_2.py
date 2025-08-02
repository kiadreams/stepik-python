class Countdown:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        self.value += 1
        return self

    def __next__(self):
        self.value -= 1
        if self.value > -1:
            return self.value
        else:
            raise StopIteration


for i in Countdown(3):
    print(i)

print()

for i in Countdown(10):
    print(i)
