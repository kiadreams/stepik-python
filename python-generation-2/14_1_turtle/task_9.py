import turtle


def line(length):
    turtle.forward(length)
    turtle.backward(length)


for _ in range(12):
    line(70)
    turtle.left(30)
