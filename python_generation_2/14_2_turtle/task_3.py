from time import sleep
import turtle


def draw_ray(lennth):
    turtle.shape('triangle')
    turtle.forward(lenght)
    turtle.stamp()
    turtle.backward(lenght)

n, lenght = int(input()), 150

turtle.pensize(2)
turtle.dot(20)
for _ in range(n):
    draw_ray(150)
    turtle.left(360 / n)


sleep(3)

