import turtle as t

t.hideturtle()
t.Screen().bgcolor('white')

def move(x, y):
  t.speed(0)
  t.penup()
  t.goto(x, y)
  t.pendown()


move(-100, -100)
for _ in range(8):
    t.speed(0)
    t.pensize(8)
    t.forward(100)
    t.left(45)

move(-97, -92)
t.pencolor('white')
t.fillcolor('red')
t.begin_fill()
for _ in range(8):
    t.speed(0)
    t.pensize(8)
    t.forward(94)
    t.left(45)
t.end_fill()

move(-154, -8)
t.fillcolor('white')
t.pencolor('black')
t.write('STOP', font=('arial', 58, 'bold'))
