with open('17_4_files/goats.txt', encoding='utf-8') as f_goats:
    f_goats.readline()
    colors = {}
    while (line := f_goats.readline().rstrip()) != 'GOATS':
        colors.setdefault(line, 0)
    goats = [g.rstrip() for g in f_goats.readlines()]
num_of_goats = len(goats)
for goat in goats:
    colors[goat] += 1
answer = filter(lambda x: (colors[x] * 100 / num_of_goats) > 7, colors)
with open('17_4_files/answer.txt', 'w', encoding='utf-8') as f_answer:
    print(*sorted(answer), sep='\n', file=f_answer)
