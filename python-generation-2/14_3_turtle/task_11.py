import turtle as t
from random import randrange as r


t.hideturtle()
t.colormode(255)
t.setup(1200, 600)
t.bgcolor('#1F295A')
t.speed(0)


def circle(radius, name, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    if num_1 == 5:
        a = radius * 1.25
        b = radius / 100 * 45 * 1.25
        t.left(90)
        t.penup()
        t.forward(45 // 2)
        t.pendown()
        t.right(90)
        t.pencolor('white')
        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 90)
        t.circle(b, 90)
        t.circle(a, 45)
        t.pencolor('black')
        t.penup()
        t.right(90)
        t.forward(45 // 2)
        t.left(90)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()
    t.pencolor('white')
    t.write(name, align='center', font=('Arial', 12, 'normal'))
    t.pencolor('black')


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def star(size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def stars(stars_num):
    st_color = (r(120, 220), r(120, 200), 255)
    step = r(3, 30)
    x = r(-1200, 600, step)
    y = r(-1200, 600, step + (step // 2))
    size = r(2, 7)
    total = int(stars_num)
    num = r(20, 200)
    while total:
        t.penup()
        t.goto(x, y)
        t.pendown()
        star(size, st_color)
        if num % 25 == 0:
            t.fillcolor(st_color)
            t.begin_fill()
            t.circle(num / 25)
            t.end_fill()
        st_color = (r(100, 220), r(100, 200), 255)
        step = r(3, 30)
        x = r(-1200, 600, step)
        y = r(-1200, 600, step + (step // 2))
        size = r(3, 10)
        turn = r(180)
        num = r(20, 200)
        total -= 1


n = 100 # количество звёзд
stars(n)
# in tuple: size, name, distance, color
planets = {0: [110, 'Солнце', 150, 'yellow'], 1: [20, 'Меркурий', 80, 'orange'],
           2: [30, 'Венера', 80, 'brown'], 3: [30, 'Земля', 80, 'blue'],
           4: [28, 'Марс', 130, 'red'], 5: [70, 'Юпитер', 150, 'brown'],
           6: [72, 'Сатурн', 130, 'orange'], 7: [45, 'Уран', 100, 'brown'],
           8: [48, 'Нептун', 100, 'cyan'], 9: [15, 'Плутон', 80, 'gray']}
rad = 90
num_1 = 0
exp = 150
for i in range(10):
    move(-600 + exp, -planets[i][0])
    circle(planets[i][0], planets[i][1], planets[i][3])
    exp += planets[i][2]
    num_1 = i
