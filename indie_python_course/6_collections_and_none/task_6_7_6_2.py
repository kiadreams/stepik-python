letters = {'a': [0, 3, 5, 7, 10], 'b': [1, 8], 'r': [2, 9], 'c': [4], 'd': [6]}


word = [' ']
for k, v in letters.items():
    # if max(v) + 1 > len(word):
    word += [' '] * (max(v) - len(word) + 1) if max(v) - len(word) + 1 > 0 else []
    for i in v:
        word[i] = k
print(''.join(word))

print()
# второй вариант...
word = {i: k for k, v in letters.items() for i in v}
print(''.join([word[i] for i in sorted(word)]))
