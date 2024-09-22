with open('words.txt', encoding='utf=8') as f:
    words = {word for word in f.read().upper().split() if word[-2:] == 'ЕЯ'}
words = sorted(words, key=lambda x: (len(x), x))
print(*words, sep='\n')
