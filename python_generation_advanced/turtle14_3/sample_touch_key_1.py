import turtle


def move_up():                            # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y + 5)
  
def move_down():                          # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y - 5)
  
def move_left():                          # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x - 5, y)

def move_right():                         # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x + 5, y)

turtle.showturtle()                        # отображаем черепашку
turtle.pensize(3)                          # устанавливаем размер пера
turtle.shape('turtle')
turtle.Screen().listen()                 # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')       # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')   # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')   # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right') # регистрируем функцию на нажатие клавиши направо

input()