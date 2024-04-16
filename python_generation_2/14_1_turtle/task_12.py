import turtle


def zigzag(side):
    for _ in range(2):
        turtle.right(90)
        turtle.forward(side)


length = 130
turtle.setheading(-90)
turtle.forward(length)
for _ in range(26):
    length -= 5
    zigzag(length)

