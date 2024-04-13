from random import randint


with open('17_4_files/random.txt', 'w', encoding='utf-8') as f:
    f.writelines('\n'.join([str(randint(111, 777)) for _ in range(25)]))
    # print(*[randint(111, 777) for _ in range(25)], sep='\n', file=f)
