import turtle
from random import randrange, randint


turtle.Screen().setup(600, 600)
turtle.Screen().bgcolor('#ddf5f7')
turtle.Screen().colormode(255)


def star(size):
    for i in range(2):
        turtle.speed(0)
        turtle.forward(size)
        turtle.right(45)
        turtle.forward(size)
        turtle.right(135)


def light(size):
    turtle.speed(0)
    turtle.forward(size*2)
    for _ in range(2):
        for _ in range(2):
            turtle.speed(0)
            turtle.right(45)
            turtle.forward(size)
            turtle.right(180)
            turtle.forward(size)
            turtle.right(45)
        turtle.right(180)
        turtle.forward(size)
    turtle.right(180)
    turtle.forward(size * 4)
    turtle.right(180)


def snowflake(size, color=[0, 0, 0]):
    turtle.pencolor(color)
    for _ in range(8):
        turtle.speed(0)
        star(size)
        light(size)
        turtle.right(45)


def snow_pos(pos_x, pos_y):
    turtle.penup()
    turtle.goto(pos_x, pos_y)
    turtle.pendown()


n = input('Введите количество снега (целое число): ')
while not n.isdigit():
    n = input('Пожалуйста, ведите число: ')
total_snow = int(n)

while total_snow:
    color_lst = [randrange(256) for n in range(3)]
    x = randrange(-300, 300, 10)
    y = randrange(-300, 300, 10)
    snow_size = randint(3, 10)
    snow_pos(x, y)
    snowflake(snow_size, color_lst)

    total_snow -= 1
