from time import sleep
import turtle


def zigzag(wight, hight):
    turtle.forward(wight)
    turtle.dot()
    turtle.left(90)
    turtle.forward(hight)
    turtle.dot()
    turtle.left(90)


for _ in range(2):
    zigzag(120, 60)
sleep(3)