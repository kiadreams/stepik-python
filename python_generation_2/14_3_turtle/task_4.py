import time
import turtle

color_lst = ('#D70F0F', '#EB9A2F', '#F5EB49', '#AFF554', '#57ED53', '#5EF4E6', '#2499F4', '#563EE3', '#D324F4', '#F4243E')

rad = 150
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.pensize(1)
for color in color_lst:
    turtle.speed(9)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(15)
    turtle.pendown()
    turtle.right(90)
    rad -= 15

time.sleep(3)
