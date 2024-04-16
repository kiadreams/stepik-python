import turtle


def star(side):
    turtle.left(36)
    for _ in range(5):
        turtle.forward(side)
        turtle.left(144)


star(70)
