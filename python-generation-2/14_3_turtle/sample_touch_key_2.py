import turtle

speed = 5
def move_up():                             # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y + speed)
  
def move_down():                           # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y - speed)

def move_left():                           # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x - speed, y)

def move_right():                          # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x + speed, y)
  
def change():                              # функция обратного вызова
  if turtle.isvisible():
    turtle.up()
    turtle.hideturtle()
  else:
    turtle.down()
    turtle.showturtle()
    
def speed_increase():                      # функция обратного вызова
  global speed
  speed += 1

def speed_decrease():                      # функция обратного вызова
  global speed
  speed -= 1

turtle.showturtle()                        # отображаем черепашку
turtle.pensize(3)                          # устанавливаем размер пера
turtle.Screen().listen()                   # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')       # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')   # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')   # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right') # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')

input()