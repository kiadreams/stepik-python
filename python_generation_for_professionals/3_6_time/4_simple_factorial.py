from math import factorial                   # функция из модуля math     
import time


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

start = time.perf_counter()

n = 500
# result = factorial_recurrent(n)
# print(result)
# result = factorial_classic(n)
# print(result)
print(factorial(n))

finish = time.perf_counter()
print(finish - start)