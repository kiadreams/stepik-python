import turtle
import time

from random import randrange


turtle.Screen().bgcolor('yellow')  #  устанавливаем цвет фона

tim = turtle.Turtle()    # создаем первую черепашку и устанавливаем ее свойства
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)


alex = turtle.Turtle()    # создаем вторую черепашку и устанавливаем ее свойства
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)


time.sleep(3)
