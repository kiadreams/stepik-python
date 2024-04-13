result = []
with open('18_1_exam/temp.txt', encoding='utf-8') as f:
    for line in f:
        if line[0] == '#':
            f.readline()
        elif line.startswith('def '):
            result.append(line[4:].split('(')[0])
if result:
    print(*result, sep='\n')
else:
    print('Best Programming Team')