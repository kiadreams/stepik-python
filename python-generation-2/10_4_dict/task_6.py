n, phone_directory = int(input()), {}
for _ in range(n):
    number, name = input().split()
    phone_directory.setdefault(name.lower(), []).append(number)
for _ in range(int(input())):
    print(*phone_directory.get(input().lower(), ['абонент не найден']))
