from contextlib import contextmanager
import time


@contextmanager  # создает для генератора методы __enter__ и __exit__
def my_time():
    start, end = time.time(), 0  # здесь выполняется метод __enter__
    yield lambda: end - start  # задесь возвращается результат из __enter__
    end = time.time() # здесь выполняется метод __exit__


with my_time() as timer:  # здесь в переменной timer присваивается lambda
    time.sleep(1.3)  # здесь ждём основной поток 1.3 сек
print(timer())  #  здесь выходим из контекста, выполняется __exit__ и меняет
# значение end после чего вызываем функцию lambda присвоенную timer



# Тоже, что и выше, только через класс----------------------------------------
def calculate():
    for i in range(1000000):
        2 ** 2123


class Timer:
    def __enter__(self):
        self.start = time.time()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = time.time()


with Timer() as my_timer:
    time.sleep(0.6)
print(my_timer())

with Timer() as my_timer2:
    time.sleep(1.5)
print(my_timer2())

with Timer() as timer_calc:
    calculate()
print(timer_calc())