# INTERSECTION ИЛИ ПО ДРУГОМУ ПЕРЕСЕЧЕНИЕ (метод intersection или "&"):
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
set_c = set_a.intersection(set_b)
print(set_c)
# Второй вариант выполнения intersection:
set_c1 = set_b & set_a
print(set_c1)
print(f'set_c и set_c1 равны? - {set_c == set_c1}')
print()

# UNION ИЛИ ПО ДРУГОМУ ОБЪЕДИНЕНИЕ (метод union или "|"):
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
set_c = set_a.union(set_b)
print(set_c)
# Второй вариант выполнения union:
set_c1 = set_b | set_a
print(set_c1)
print(f'set_c и set_c1 равны? - {set_c == set_c1}')
print()

# DIFFERENCE ИЛИ ПО ДРУГОМУ РАЗНОСТЬ (метод intersection или "-"):
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
set_c = set_a.difference(set_b)
print(set_c)
# Второй вариант выполнения difference:
set_c1 = set_a - set_b
print(set_c1)
print(f'set_c и set_c1 равны? - {set_c == set_c1}')
print()

# SYMMETRIC DIFFERENCE ИЛИ ПО ДРУГОМУ РАЗНОСТЬ
# (метод symmetric_difference или "^"):
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# Второй вариант выполнения difference:
set_c1 = set_b ^ set_a
print(set_c1)
print(f'set_c и set_c1 равны? - {set_c == set_c1}')
print()
