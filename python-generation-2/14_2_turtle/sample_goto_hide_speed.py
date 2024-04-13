import time
import turtle


# Команды turtle.setposition() и turtle.setpos() аналогичны команде turtle.goto(). Все три команды перемещают черепашку в заданную позицию.

turtle.speed(1)
turtle.goto(0, 100)
time.sleep(1)
turtle.speed(5)
turtle.hideturtle()
time.sleep(1)
print(turtle.pos())
turtle.setposition(-100, 0)
turtle.speed(10)
time.sleep(1)
turtle.showturtle()
time.sleep(1)
print(turtle.pos())
turtle.setpos(0, 0)
print(turtle.pos())
time.sleep(1)
turtle.speed(0) # Отключает анимацию перемещения
turtle.goto(100, 0)
time.sleep(1)
for i in range(1, 11):
    turtle.speed(i)
    turtle.circle(100 - 10*i)




time.sleep(2)