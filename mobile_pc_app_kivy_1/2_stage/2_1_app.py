from kivy.app import App
from kivy.config import Config

# Изменяем размеры окна на 400*700 px
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
# отключаем режим масштабирования окна
# Config.set("graphics", "resizable", "0")


class FirstApp(App):
    pass


if __name__ == "__main__":
    FirstApp().run()
