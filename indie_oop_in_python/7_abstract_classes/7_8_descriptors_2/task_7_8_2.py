class ColourComponent:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return int(instance.hex[self.start:self.end], base=16)


class Colour:
    r = ColourComponent(1, 3)
    g = ColourComponent(3, 5)
    b = ColourComponent(5, 7)

    def __init__(self, hex):
        self.hex = hex


colour = Colour("#abcded")
print(colour.r)
print(colour.g)
print(colour.b)
print()
cc = ColourComponent(1, 3)
print(cc.start)
print(cc.end)