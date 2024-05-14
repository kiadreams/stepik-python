import time

import turtle


colors_circle = {'red': (0, 60), 'yellow': (0, -40), 'green': (0, -140)}
coordinates_rect = ((60, -155), (60, 155), (-60, 155), (-60, -155))

turtle.penup()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.goto(-60, -155)
turtle.pendown()

for i in coordinates_rect:
    turtle.goto(i)

turtle.end_fill()

for k, v in colors_circle.items():
    turtle.pendown()
    turtle.goto(v)
    turtle.fillcolor(k)
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()

time.sleep(3)
