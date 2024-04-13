import turtle
import time


turtle.write('Привет черепашка')

# turtle.Screen().setup(400, 300)
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху')
turtle.goto(50, -120)
turtle.write('Снизу')
turtle.goto(100, 20)
turtle.write('Справа')

turtle.goto(-120, 120)
turtle.write('Сверху', move=True, align='center', font=('Arial', 17, 'bold'))
turtle.goto(50, -120)
turtle.write('Снизу', move=True, align='left', font=('Times New Roman', 25, 'normal'))
turtle.goto(100, 20)
turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))

turtle.forward(100)
turtle.begin_fill()     # включаем заливку
turtle.circle(80)
turtle.end_fill()       # выключаем заливку

turtle.goto(turtle.pos() - (0, 300))
turtle.fillcolor('red') # выставаляем цвет заливки
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.goto(turtle.pos() - (200, 0))
turtle.fillcolor('green')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.goto(turtle.pos() + (-200, -200))
turtle.begin_fill()      # Цвет заполнения остался с предыдущего указания по заполнению квадрата
turtle.goto(-50, 120)
turtle.goto(120, 120)
turtle.goto(150, -80)
turtle.end_fill()


time.sleep(3)
