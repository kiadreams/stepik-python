import turtle as t


bg_color = '#000BCB'
t.Screen().setup(500, 500)
t.Screen().bgcolor(bg_color)

def circle(rad, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()


x = 0
y = -150
num = 800
t.hideturtle()
t.speed(0)
t.tracer(0)
while num:
    circle(150, 0, -150, '#FFCE00')
    circle(150, x + 300, y, bg_color)
    x -= 1
    num -= 1
    t.update()
