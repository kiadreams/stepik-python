

# !!!Для сравнения переменной с None всегда используйте оператор is. Для встроенных типов поведение is и == абсолютно одинаково, однако с пользовательскими типами могут возникнуть проблемы, так как в Python есть возможность переопределения операторов сравнения в пользовательских типах.!!!

var = None
if var is None:  # используем оператор is
  print('None')
else:
  print('Not None')

print()

print(bool(None))

