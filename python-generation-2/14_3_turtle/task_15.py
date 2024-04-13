import turtle as tt
from random import randrange as rr

def rcl():
  return rr(256), rr(256), rr(256) 
  
def zv(x, y, n, r, cl, an):
    tt.goto(x, y)
    tt.color(cl)
    tt.begin_fill()
    for _ in range(n):
        tt.forward(r)
        tt.right(an)
        tt.forward(r)
        tt.left(an)
        tt.right(360/n)
    tt.end_fill()
    tt.update()

def left_mouse_click(x, y):
    zv(x, y, rr(3, 10), rr(10, 40), rcl(), rr(140, 210))


tt.colormode(255)
tt.tracer(0)
tt.hideturtle()
tt.penup()
tt.Screen().bgcolor('black')

tt.Screen().onclick(left_mouse_click)
tt.Screen().listen()

input()