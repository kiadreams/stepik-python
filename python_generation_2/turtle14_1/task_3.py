import turtle


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


for _ in range(3):
    turtle.left(20)
    square(150)

n = input()