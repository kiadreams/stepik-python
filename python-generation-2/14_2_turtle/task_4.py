from time import sleep
import turtle


def draw_ray(some_len):
    turtle.penup()
    turtle.forward(some_len)
    turtle.stamp()
    turtle.backward(some_len)


lenght = 100

turtle.shape('turtle')
turtle.pensize(3)
turtle.stamp()
for _ in range(10):
    draw_ray(lenght)
    turtle.left(36)


sleep(3)
