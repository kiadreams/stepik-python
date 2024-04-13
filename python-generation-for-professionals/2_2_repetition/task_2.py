# # Мой вариант №1
# letters = [input() for _ in range(3)]
# result = sum(map(lambda x: ord(x) < 1000, letters))
# if result == 3:
#     print('en')
# elif result == 0:
#     print('ru')
# else:
#     print('mix')

# Мой вариант №2
answer = ('ru', 'mix', 'mix', 'en')
english_letters = 'AaBCcEeHKMOoPpTXxy'
result = sum([input() in english_letters for _ in range(3)])
print(answer[result])

# english_letters = list(map(ord, 'AaBCcEeHKMOoPpTXxy'))
# russian_letters = list(map(ord, 'АаВСсЕеНКМОоРрТХху'))
# print(english_letters)
# print(russian_letters)