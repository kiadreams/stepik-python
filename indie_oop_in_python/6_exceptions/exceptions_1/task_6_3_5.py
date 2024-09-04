class CustomButton:

    def __init__(self, text: str, **kwargs):
        self.text = text
        self.__dict__.update(kwargs)

    def config(self, **kwargs):
        self.__dict__.update(kwargs)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")


btn = CustomButton(text="Hello", siria=31, passport="first")
print(dir(btn), "\n")
btn.config(command="upps!")
print(dir(btn))
btn.click()
