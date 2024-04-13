count = int(input())
result = set(input().split(', '))
result.intersection_update(*[input().split(', ') for _ in range(count -1)])
if result:
    print(*sorted(result), sep=', ')
else:
    print('Сериал снять не удастся')

    