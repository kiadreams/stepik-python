import time
import turtle as turt
from math import sin, pi, cos


t = 0.0
turt.color("red")
turt.begin_fill()
while t < 2*pi:
    turt.goto(128*sin(t)**3, 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5))
    t += 0.01
turt.end_fill()

time.sleep(3)
