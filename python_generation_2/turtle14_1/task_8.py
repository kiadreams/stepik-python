import turtle


def rhombus(side):
    for _ in range(2):
        for _ in range(2):
            turtle.forward(side)
            turtle.left(60)
        turtle.left(60)


for _ in range(10):
    rhombus(70)
    turtle.left(36)
