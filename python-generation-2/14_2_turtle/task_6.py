from time import sleep
import turtle


def zigzag(quantity):
    way = 1
    for _ in range(6 * quantity):
        turtle.forward(way)
        turtle.stamp()
        turtle.right(20)
        way += 1


turtle.shape('turtle')
turtle.pensize(3)
turtle.penup()
turtle.stamp()
turtle.Screen().bgcolor('lawngreen')
zigzag(7)



sleep(3)
