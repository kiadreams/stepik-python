import turtle


def hexagon(side):
    for _ in range(6):
        turtle.left(60)
        turtle.forward(side)


hexagon(100)