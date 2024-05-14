import turtle


def hexagon(side):
    for _ in range(6):
        turtle.right(60)
        turtle.forward(side)


side = int(input())
for _ in range(6):
    turtle.forward(side)
    hexagon(side)
    turtle.left(60)
