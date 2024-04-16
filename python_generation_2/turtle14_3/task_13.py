import tkinter
import turtle as t
import random as r

# получим разрешение экрана. Подсмотрено в интернете
root = tkinter.Tk()
root.withdraw()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()  # автополучение параметров экрана
# полный экрна. Подсмотрено
screen = t.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

def draw_some_stars():    # рисует небо и звёзды
    t.bgcolor(sky_color)  # цвет неба
    t.tracer(0)
    t.pencolor(star_color)
    for _ in range(width*height//4000):  # кол-во звёзд, считает автоматически, исходя из размеров поля
        starsize = r.randint(1,3)
        t.penup()
        t.goto(r.randint(-width//2, width//2), r.randint(-height//2, height//2))
        t.pendown()
        t.dot(starsize)

def tower_calculate(towers_height, place, layer):
    tower_w = r.randint(width // (layer*12), width // (layer*6))  # ширина башни
    tower_h = r.randint(towers_height[0] // 5, towers_height[1] // 5) * (height // 20)  # высота башни
    apartaments_on_floor = r.randint(6, 8)
    sleep = r.uniform(0.6, 0.9)  # не спящих от 0 до 1. Работает весьма приблизительно
    cornerstone = (place, -height/2 + tower_h)  # верхний левый угол башни. Опорный
    return cornerstone, tower_w, tower_h, apartaments_on_floor, sleep

def wind_calculate(tower_w, tower_h, number_of_windows):  # переместить после функции рисования неба
    # ширина, высота окна
    section = tower_w / number_of_windows
    wind_width = section * 0.6
    wind_height = wind_width * 1.2
    
    # определяем промежутки между окнами
    x_space = (section - wind_width) / 2
    y_space = wind_height / 3
    floor = int(tower_h / (wind_height + y_space))
    
    return floor, (wind_width, wind_height), (x_space, y_space)

def draw_tower(place, tower_w, tower_h, tower_color):  # рисует башни по одной
    t.penup()
    t.goto(place, -height/2)  # рисование с левого нижнего угла башни
    
    t.setheading(90)
    t.pendown()
    t.fillcolor(tower_color)
    t.begin_fill()
    for i in range(2):
        t.forward(tower_h)
        t.right(90)
        t.forward(tower_w)
        t.right(90)
    t.end_fill()

def get_color(flashing, layer):  # варьирует цвет окна
    if flashing:
        if r.randint(0, 1):      # выберем, включить или выключить окно
            return towers_height_and_colors[1][1]  # и если выбирается 1, то окно выключается 
    if r.randint(0, 100) < 3:    # 3 = % розовых
        return '#ff30ff'
    R, G, B = 255, 251, 255
    lr = layer
    Rhex = str(hex(r.randint(R - ((lr) * 50),  R - ((lr-1) * 50)))[2:]).ljust(2, '0')
    Ghex = str(hex(r.randint(G - ((lr) * 50),  G - ((lr-1) * 50)))[2:]).ljust(2, '0')
    Bhex = str(hex(r.randint(B - ((lr) * 60),  B - ((lr-1) * 30)))[2:]).ljust(2, '0')   # читабельность
    
    return '#' + Rhex + Ghex + Bhex

# рисует окно
def draw_the_window(cornerstone, window_size, window_space, floor, apart_number, layer, tower_color, tracer=0,  flashing=False):
    wind_width, wind_height = window_size
    x_space, y_space = window_space
    #идём на cornerstone здания
    t.penup()
    t.tracer(tracer)
    t.goto(cornerstone)
    
    x_start = wind_width * (apart_number-1) + x_space + x_space*((apart_number-1)*2)  # идем на угол окна. тяжело читать эту формулу
    y_start = wind_width * (floor-1) +  y_space + y_space*((floor - 1)*2)
    
    t.goto(cornerstone[0]+x_start, cornerstone[1]-y_start)
    
    # собственно рисование
    t.pencolor(tower_color)
    t.fillcolor(get_color(flashing, layer))
    t.begin_fill()
    t.pendown()
    for _ in range(2):
        t.right(90)
        t.forward(wind_width)
        t.right(90)
        t.forward(wind_height)
    t.penup()
    t.end_fill()
    t.pencolor(sky_color)

# вызывает все функции в нужном порядке,
def draw_all(layer, towers_height, towers_color):
    place = -width // 2
    t.pencolor(sky_color)
    dict_of_towers = {}  # координаты всех домов и окон, для анимации после отрисовки
    while place < width / 2:
        cornerstone, tower_w, tower_h, apartaments_on_floor, sleep = tower_calculate(towers_height, place, layer)  # получаем параметры домов,..
        floors, window_size, window_space = wind_calculate(tower_w, tower_h, apartaments_on_floor)                 # ...окон
        draw_tower(place, tower_w, tower_h, towers_color)
        
        windows_dict = {i: tuple(set(r.randint(1, apartaments_on_floor) for i in range(r.randint(0, round(apartaments_on_floor*sleep))))) for i in range(2, floors)}  # словарь. этаж (счёт сверху): кортеж с номерами окон # читаемость

        dict_of_towers[(cornerstone, window_size, window_space)] = windows_dict
        
        for floor, apart_numbers in windows_dict.items():
            for apart_number in apart_numbers:
                draw_the_window(cornerstone, window_size, window_space, floor, apart_number, layer, towers_color)            
        place += tower_w
    
    return dict_of_towers

def windows_flashing():  # идёт по собранному словарю и мигаем только имеющимися окнами на первом плане
    while True:
        rand_tower = r.choice(list(dict_of_towers.items()))
        rand_floor = r.choice(list(rand_tower[1].items()))
        if len(rand_floor[1]) > 0:
            rand_window = r.choice(rand_floor[1])
            cornerstone, window_size, window_space = rand_tower[0]
            draw_the_window(cornerstone, window_size, window_space, rand_floor[0], rand_window, 3, '#04396c', tracer=1, flashing=True)

# настройки
t.hideturtle()
t.speed(0)
sky_color, star_color  = '#001e42', '#fefb89'          # цвет неба, звёзд
towers_height_and_colors = {3: ((30, 70), '#012450'),
                            2: ((22, 45), '#023065'),
                            1: ((15, 25), '#04396c')}  # слой: (вероятная этажность % от width, цвет башен)

draw_some_stars()  # рисует фон со звёздами

# послойно рисует дома
for layer, feats in towers_height_and_colors.items():
    dict_of_towers = draw_all(layer, feats[0], feats[1])

windows_flashing()  # запускает мигание окон