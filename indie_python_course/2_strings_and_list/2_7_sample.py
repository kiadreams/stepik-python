# s = 'asdf\\n dsaf\\nasd\\'
# print(s)
# b = r'asdf\\n dsaf\\nasd\\'
# print(b)
# print()
# c = 5
# print(f'{{c = }}')
# print(['q', 'w', 't'] * 15)
#
# a, *b, c = (1, 2, 4, 5)
# print(a, b, c)
# n = input().rjust(6, '0')
# print(n)
# if (l := len(n)) % 2 == 1:
#     print("NO")
# elif sum(map(int, n[: l // 2])) == sum(map(int, n[l // 2:])):
#     print('YES')
# else:
#     print('NO')
lang = "rust"

match lang:
    case "с++":
        print("Это сиииии...")
    case "java" | "python" | "rust":
        print("это один из моих любимых языков, которые я хочу выучить!!!")
    case "c#":
        print("Это сишарп...")
    case _:
        print("Язык не важен")

print()

direction = 'NoRtH'
match direction.lower():
    case "north" | "east" | "south" | "west":
        print("Хорошо, я пошел!")
    case _:
        print("Неизвестное направление...")

print()

# ЛЕГКАЯ ПРОВЕРКА ТИПА ПЕРЕМЕННОЙ!!!
# меняйте значение переменной value
value = [1, 2, 3]

match value:
    case [1, 2]:
        print("Не понял...")
    case int() | float():
        print("Имеем дело с числом")
    case str():
        print("Имеем дело со строкой")
    case list():
        print("Имеем дело со списком")
    case  _:
        print("Лучше с этим дел не иметь")