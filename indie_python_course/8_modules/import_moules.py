import sys
from string import ascii_lowercase, ascii_uppercase, punctuation

from proba import some_f

print(sys.getrecursionlimit())
print(sys.path)
some_f()
print(f'some_f() запускается в модуле с именем - {__name__}')
print()
print(ascii_lowercase)
print(ascii_uppercase)
print(punctuation)