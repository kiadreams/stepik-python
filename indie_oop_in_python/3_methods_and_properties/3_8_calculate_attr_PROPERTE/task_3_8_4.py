class Colour:

    def __init__(self, hex_color):
        self.hex_color = hex_color
        self.__red = None
        self.__green = None
        self.__blue = None

    @property
    def red(self):
        if self.__red is None:
            self.__red = int(self.hex_color[1:3], base=16)
        return self.__red

    @property
    def green(self):
        if self.__green is None:
            self.__green = int(self.hex_color[3:5], base=16)
        return self.__green

    @property
    def blue(self):
        if self.__blue is None:
            self.__blue = int(self.hex_color[5:], base=16)
        return self.__blue


# Проверкa------------------------------------------------------------------------
# Тест1
colour = Colour("#ff0000")
print(colour.red)
print(colour.green)
print(colour.blue)
print()

# Тест2
colour = Colour("#00ff2d")
print(colour.red)
print(colour.green)
print(colour.blue)
print()

# Тест3
colour = Colour("#aacce4")
print(colour.red)
print(colour.green)
print(colour.blue)
print()
