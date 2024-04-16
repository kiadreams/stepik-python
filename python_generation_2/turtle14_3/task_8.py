import turtle as t
from random import randrange as r
from math import sin, pi

t.Screen().setup(600, 600)

def polygon(length, num, color2):
    size = sin(pi / num) * (length / pi)
    t.fillcolor(color2)
    t.begin_fill()
    for _ in range(num):
        if num == 3 or num == 4:
            t.forward(size + size // 4)
        else:
            t.forward(size)
        t.right(360 / num)
    t.end_fill()

def colors():
    shape_color = (r(256), r(256), r(256))
    return shape_color

def move(x1, y1):
    t.penup()
    if numb == 3 or numb == 4:
        t.goto(x1 - (100 // 5), y1)
    else:
        t.goto(x1, y1)
    t.pendown()

t.hideturtle()
t.colormode(255)
t.speed(0)
for y in range(-200, 300, 100):
    for x in range(-200, 300, 100):
        numb = r(3, 9)
        move(x, y)
        polygon(250, numb, colors())
