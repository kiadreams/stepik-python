class Point:
    def __init__(self):
        print('Init Point')


class Square:
    def __new__(cls):
        print('new of Square')
        return super().__new__(Square)

    def __init__(self):
        print('Init Square')


x = Square()
print(x)