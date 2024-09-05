class MyException(Exception):
    pass

try:
    raise MyException("hello", 1, 2, 3)
except MyException:
    print("done")
