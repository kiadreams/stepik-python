import turtle


def rhombus(side):
    for _ in range(2):
        for _ in range(2):
            turtle.forward(side)
            turtle.left(120)
        turtle.right(60)


rhombus(70)