from time import sleep
import turtle


def draw_ray(some_len):
    part_len = some_len // 10
    turtle.penup()
    turtle.forward(7 * part_len)
    turtle.pendown()
    turtle.forward(2 * part_len)
    turtle.penup()
    turtle.forward(1 * part_len)
    turtle.stamp()
    turtle.backward(some_len)


lenght = 100

turtle.shape('turtle')
turtle.pensize(3)
turtle.stamp()
turtle.Screen().bgcolor('cyan')
for _ in range(10):
    draw_ray(lenght)
    turtle.left(36)


sleep(3)
