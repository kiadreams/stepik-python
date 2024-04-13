import turtle

turtle.shape('square')
turtle.forward(100)
turtle.setheading(90)

turtle.shape('arrow')
turtle.forward(100)
turtle.setheading(180)

turtle.shape('turtle')
turtle.forward(100)
turtle.setheading(270)

turtle.shape('circle')
turtle.forward(100)
num = input()

# Так устанавливается и задаётся своё изоображение черепашки!!!
turtle.Screen().addshape('rocketship.gif')  # регистрируем изображение
turtle.shape('rocketship.gif')              # устанавливаем изображение


for _ in range(4):
    turtle.forward(150)
    turtle.left(90)
