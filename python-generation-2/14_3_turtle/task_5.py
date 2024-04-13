
import time
import turtle

a = 200
r = 70

def square(a):
    turtle.up()  
    turtle.goto(-a/2, a/2)
    #turtle.down()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.end_fill()

def circ(r, color,d):
    turtle.up()  
    turtle.goto(0+d, -r)
    #turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

square(a)
circ(r,'orange', 0 )
circ(r,'blue', 20 )

time.sleep(3)
