string = input().split()
answer, counter = [], {}
for letter in string:
    if c := counter.setdefault(letter, []):
        answer.append(f'{letter}_{len(c)}')
    else:
        answer.append(letter)
    counter.get(letter, []).append(letter)
print(' '.join(answer))
