import time
import turtle as tt
import random as rr

def zv(coord, clr):  # звезды
    xl, yb, w, h = coord
    if w > 10:
        tt.fillcolor(clr)
        tt.pencolor(clr)
        for _ in range(rr.randint(2, 5)):
            r = rr.randint(1, 3)
            pt = (rr.randint(xl + r, xl + w - r),
                  rr.randint(yb + r, yb + h - r))
            tt.goto(pt)
            tt.begin_fill()
            tt.circle(r)
            tt.end_fill()

def fig(coord, clr):  # здания
    xl, yb, w, h = coord
    cont = [(xl, yb), (xl, yb + h), (xl + w, yb + h), (xl + w, yb), (xl, yb)]
    tt.fillcolor(clr)
    tt.pencolor(clr)
    tt.goto(cont[0])
    tt.pendown()
    tt.begin_fill()
    for pt in cont: 
        tt.goto(pt)
    tt.end_fill()
    tt.penup()

def win(coord, clr):   # окна
    r = 15
    xl, yb, w, h = coord
    if w > 30:
        for _ in range(rr.randint(0, 2)):
            x, y = xl + r * rr.randrange(w // r), yb + r * rr.randrange(h // r)
            pt = [x, y, r, r]
            fig(pt, clr)

# начало основной программы


tt.colormode(255)
tt.speed(0)
tt.tracer(0)
tt.hideturtle()
tt.penup()
hcl = (20, 20, 160)
wcl = (255, 255, 150)
bcl = (5, 5, 70)

xp, yp, wp, hp = -180, -180, 380, 360
kv = [xp, yp, wp, hp]

fig(kv, bcl)   # небо

x = xp
while x < wp + xp:
    w = rr.randint(50, 80)
    if x + w > wp + xp: 
      w = wp + xp - x
    h = rr.randint(60, 240)
    kv = [x, yp, w, h]
    fig(kv, hcl)    # здания
    kv = [x + 5, yp + 5, w - 10, h - 10]
    win(kv, wcl)    # окна
    kv = [x, yp + h, w, hp - h]
    zv(kv, wcl)     # звезды
    x = x + w

tt.update()


time.sleep(2)
