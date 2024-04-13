phrase, counter = input().split(), {}
for i, word in enumerate(phrase):
    number = counter.setdefault(word, 0) + 1
    phrase[i] = number
    counter[word] = number
print(*phrase)