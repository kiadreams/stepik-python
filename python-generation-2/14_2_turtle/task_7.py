from time import sleep
import turtle


color_lst = ['yellow', 'blue', 'red', 'orange', '#be54d4', 'green']

def line(rows):
    way, size = 150, 15
    part, d_size = way // (rows * 7), 20 // rows
    for i in range(rows):
        turtle.pensize(size)
        for j in range(7):
            color = color_lst[(i + j) % 6]
            turtle.pencolor(color)
            turtle.forward(way)
            turtle.right(45)
            way -= part
        size -= d_size


turtle.Screen().bgcolor('cyan')
line(8)

sleep(3)
