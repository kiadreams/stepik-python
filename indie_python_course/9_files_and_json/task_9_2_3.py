with open('lorem.txt', encoding='utf-8') as f:
    words = {}
    for word in f.read().upper().split():
        words[word] = words.get(word, 0) + 1
print(words)