import time
import turtle


def draw_circles(dots):
    for dot in dots:
        turtle.penup()
        turtle.goto(dot)
        turtle.pendown()
        turtle.circle(dots.get(dot))


def finished_beer():
    for i in range(2):
        turtle.penup()
        turtle.goto([(-90, 30), (90, 30)][i])
        turtle.pendown()
        turtle.dot(30)
    turtle.penup()
    turtle.goto(0, -15)
    turtle.pendown()
    turtle.goto(0, -85)
    

radiuses = [40, 40, 163, 100, 20]
centers = [(-130, 130), (130, 130), (0, -150), (0, -149), (0, -15)]
turtle.pensize(3)
all_dots = dict(zip(centers, radiuses))
draw_circles(all_dots)
finished_beer()

time.sleep(3)
