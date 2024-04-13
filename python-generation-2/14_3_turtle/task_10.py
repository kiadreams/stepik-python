import time
import turtle as t

lst = ['Восток', 'Запад', 'Север', 'Юг']
lst1 = ['left', 'right', 'center', 'center']

def line(size):
    for i in range(2):
        for y in range(2):
            t.forward(size)
            t.penup()
            t.forward(size // 4)
            t.write(lst[y + i + i], align=lst1[y + i + i])
            t.left(180)
            t.forward(size // 4)
            t.pendown()
            t.forward(size)
        t.left(90)
    t.penup()
    t.goto(0, size // 4)
    t.pendown()
    t.circle(size // 4)


t.speed(0)
t.hideturtle()
line(100)

time.sleep(3)
