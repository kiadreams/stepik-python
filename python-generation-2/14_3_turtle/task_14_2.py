import turtle as t
from random import randint


res_x = 1920
res_y = 1080
shift_x = -0.5
shift_y = 0
scale = -100


def is_part_of(x, y):
    c = complex((x / (res_y / 2 + scale) + shift_x), y / (res_y / 2 + scale) + shift_y)
    z = 0
    n = 0
    for _ in range(300):
        z = z ** 2 + c
        n += 1
        if abs(z) > 10:
            if 1 <= n <= 5: 
                return t.dot(2, (255, 0, 255))
            elif 6 <= n <= 10: 
                return t.dot(2, (0, 0, 255))
            elif 11 <= n <= 15: 
                return t.dot(2, (0, 255, 255))
            elif 16 <= n <= 20: 
                return t.dot(2, (0, 255, 0))
            elif 21 <= n <= 25: 
                return t.dot(2, (255, 255, 0))
            elif 26 <= n <= 30: 
                return t.dot(2, (255, 0, 0))
            elif n > 30: 
                return t.dot(2, (255, 255, 255))


t.colormode(255)
t.bgcolor('black')
t.penup()
t.speed(0)
t.tracer(1000, 1)

while True:
    t.goto(randint(-res_x // 2, res_x // 2), randint(-res_y // 2, res_y // 2))
    is_part_of(*t.pos())
    # t.update()

