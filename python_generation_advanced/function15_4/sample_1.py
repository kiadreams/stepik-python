print(type(print))
print(type(sum))
print(type(abs))
print(type(sorted))

def my_func():
    print('Вызвали my_func')
    pass

print()
print(type(my_func))

s = my_func
s()
p = print
p('заменили print()')
