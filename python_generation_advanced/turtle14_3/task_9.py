import time
import turtle as t

def square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

chess_color = ['white', 'black']
t.speed(0)
t.hideturtle()
t.tracer(0)
cnt = 0
for y in range(-150, 100, 50):
    for x in range(-150, 100, 50):
        move(x, y)
        square(50, chess_color[1])
        if cnt % 2 == 0:
            chess_color[0], chess_color[1] = 'black', 'white'
        else:
            chess_color[0], chess_color[1] = 'white', 'black'
        cnt += 1
t.update()

time.sleep(3)
