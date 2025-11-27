import math
from unittest.mock import Mock


# Работа функции math до создания mock
print(math.sqrt(9))
print(math.sqrt(100))

try:
    print(math.sqrt())
except TypeError as ex:
    print(ex)

try:
    print(math.sqrt(5, 7))
except TypeError as ex:
    print(ex)

# -----------------------------------------------------
# Ниже между двумя комментариями замокайте функцию math
math.sqrt = Mock(return_value='Квадратный корень')

# Проверяем вызов
# ---------------

print(math.sqrt(2))
print(math.sqrt(2, 5))
print(math.sqrt())