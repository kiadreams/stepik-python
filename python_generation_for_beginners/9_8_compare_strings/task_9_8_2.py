strings = []
while (s := input()) != 'КОНЕЦ':
    strings.append(s)
print(
    f'Минимальная строка ⬇️: {min(strings)}',
    f'Максимальная строка ⬆️: {max(strings)}',
    sep='\n'
)
