n = int('51', 8)
print(n)
string = str(n)
print(string)
s = None
print('Проверка на равенство None True:', s == True)
print('Проверка на равенство None False:', s == False)
print('Проверка на равенство None 0:', s == 0)
if s:
    print('В условии None работает как True!!!')
elif not s:
    print('В условии None работает как False!!!')
else:
    if s is None: print('В условии None не работает ни как False ни как True!')
while s:
    print('В цикле "while" None работает как True!!!')
    s = False
s = None
while not s:
    print('В цикле "while" None работает как False!!!')
    s = True
s = None
