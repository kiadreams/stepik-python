import time
import turtle


def draw_rays(end, starts: list):
    for start in starts:
        turtle.penup()
        turtle.goto(start)
        turtle.pendown()
        turtle.dot(10, 'blue')
        turtle.goto(end)
    turtle.dot(10, 'red')

my_end = 0, 200
l_starts = [(i, 0) for i in range(-135, 165, 30)]
draw_rays(my_end, l_starts)

time.sleep(3)