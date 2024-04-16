import time
import turtle
import random


turtle.Screen().setup(1920, 1080)
turtle.colormode(255)
colors = 'red', 'orange', 'yellow', 'LimeGreen', 'LawnGreen', 'lightgreen', \
        'cyan', 'PowderBlue', 'blue', 'orchid', 'magenta', 'green', 'purple'
turtle.speed(0)
turtle.hideturtle()
for i in range(100):
    x = random.randint(-900, 900)
    y = random.randint(-500, 500)
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(random.randrange(10, 110))
    size = random.randrange(10, 35)
    turtle.pendown()
    turtle.begin_fill()
    # color = random.choice(colors)
    color = (random.randrange(255), random.randrange(255), random.randrange(255))
    turtle.pencolor(color)
    turtle.fillcolor(color)
    for j in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


time.sleep(3)
