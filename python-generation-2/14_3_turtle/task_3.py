import time
import turtle


turtle.Screen().setup(500, 500)
turtle.Screen().bgcolor('white')

# два варианта

def triangle(size):
    if turtle.isvisible():
        for _ in range(3):
            turtle.forward(size)
            turtle.left(60 * 2)
    else:
        for _ in range(3):
            turtle.pensize(size // 8)
            turtle.forward(size)
            turtle.dot()
            turtle.left(60 * 2)
        turtle.pensize(1)

def illusion(x, y):
    turtle.speed(10)
    triangle(200)
    turtle.penup()
    turtle.goto(100 + x, -50 + y)
    turtle.left(60)
    turtle.hideturtle()
    triangle(200)
    turtle.showturtle()
    turtle.fillcolor('white')
    turtle.pencolor('white')
    turtle.begin_fill()
    triangle(200)
    turtle.end_fill()
    turtle.hideturtle()
  
x, y = -80, -20
turtle.penup()  
turtle.goto(x, y)
turtle.pendown()
illusion(x, y)

time.sleep(3)