import turtle
import time


turtle.pensize(5)
turtle.circle(80)
turtle.forward(70)
turtle.dot()
turtle.right(90)
turtle.pencolor('cyan')
turtle.forward(90)
turtle.dot(10, 'black')
turtle.pencolor('red')           #  строковое представление цвета
turtle.circle(90)
print(turtle.pencolor())
tup = (0.2, 0.8, 0.55)
turtle.pencolor(tup)   #  значения r, g, b в качестве аргументов
print(turtle.pencolor())
turtle.circle(50)
turtle.colormode(255)  # Переключение с режима цвета 1.0 на 255
print(turtle.pencolor())
turtle.pencolor(255, 0, 0)
turtle.circle(45)
turtle.pencolor((200, 120, 0))
turtle.circle(40)
color = (23, 223, 123)
turtle.pencolor(color)
turtle.circle(35)
turtle.Screen().bgcolor(30, 30, 30)

turtle.left(270)
turtle.forward(200)
turtle.shape('turtle')
for i in range(3):
    turtle.stamp()
    turtle.forward(30)
time.sleep(3)

# Сброс настроек экрана
# turtle.clear() - стирает все рисунки в графическом окне. Но не меняет положение черепашки, цвет рисунка и цвет фона графического окна.
turtle.clear()
time.sleep(5)
# turtle.reset() - стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает черепашку в исходное положение в центре экрана. Эта команда не переустанавливает цвет фона графического окна.
turtle.reset()
time.sleep(5)
# turtle.clearscreen() -  стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на белый, и возвращает черепашку в исходное положение в центре графического окна
turtle.clearscreen()
time.sleep(3)

# Устанавливает размер рабочего окна
turtle.Screen().setup(640, 460)
time.sleep(3)
turtle.Screen().setup(1920, 1080)
time.sleep(3)


# Так устанавливается фоновое изоображение!!! Но не сработает так как нет фактически рисунка

turtle.Screen().setup(400, 400)               # устанавливаем размер граф. окна
turtle.Screen().addshape('rocketship.png')    # добавляем форму черепашки

# устанавливаем фоновое изображение
turtle.Screen().bgpic('space.jpg')
turtle.shape('rocketship.png')                # устанавливаем форму черепашки
turtle.pencolor('green')
turtle.pensize(5)

for _ in range(4):
  turtle.forward(150)
  turtle.left(90)
  


