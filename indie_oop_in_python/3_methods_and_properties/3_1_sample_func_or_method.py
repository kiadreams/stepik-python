class Cat:

    def say_hello(*args):
        print("Hello cat!", args)


a = Cat()
# Эта функция в классе
print(Cat.say_hello)
Cat.say_hello()
print()
# Это метод у объекта - при его вызове он автоматически передает в
# вызываемые у него метод ссылку на себя...!!!
print(a.say_hello)
a.say_hello()
