import time
import turtle as t

t.Screen().bgcolor('blue')
t.hideturtle()
t.tracer(0)
t.penup()

while True:
    for i in range(200, -200, -1):
        t.goto(0, 0)
        t.dot(200, 'orange')
        t.goto(i, 0)
        t.dot(200, 'blue')
        t.update()


time.sleep(3)
