import turtle


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


side = 15
turtle.setheading(90)
for _ in range(31):
    square(side)
    side += 5
