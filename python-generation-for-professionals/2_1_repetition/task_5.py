# Вариант первый
# def convert(string: str) -> str:
#     up_lets = sum(1 for s in string if s.isalpha() and s.isupper())
#     low_lets = sum(1 for s in string if s.isalpha() and s.islower())
#     return string.upper() if up_lets > low_lets else string.lower()


# Вариант второй
def convert(string: str) -> str:
    counter = sum(1 if s.isupper() else -1 for s in string if s.isalpha())
    return string.upper() if counter > 0 else string.lower()



print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
