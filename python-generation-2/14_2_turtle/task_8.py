import time
import turtle


def draw_triangle(side):
    turtle.pendown()
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

draw_triangle(150)
turtle.penup()
turtle.goto(150, 80)
turtle.setheading(180)

draw_triangle(150)

time.sleep(3)