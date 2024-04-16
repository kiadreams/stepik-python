words = [input().split(':') for _ in range(int(input()))]
dict_word = {k.strip(' :').lower(): v.strip(' :') for k, v in words}
for _ in range(int(input())):
    print(dict_word.get(input().lower(), 'Не найдено'))
