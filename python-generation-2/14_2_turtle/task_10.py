import time
import turtle


def draw_circles(dots):
    for dot in dots:
        turtle.penup()
        turtle.goto(dots.get(dot))
        turtle.pendown()
        turtle.pencolor(dot)
        turtle.circle(50)


colors = ['blue', 'green', 'black', 'red', 'yellow']
centers = [(-100, 30), (50, -30), (0, 30), (100, 30), (-50,-30)]
turtle.pensize(5)
all_dots = dict(zip(colors, centers))
draw_circles(all_dots)

time.sleep(3)
