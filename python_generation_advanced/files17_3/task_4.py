with open('17_3_files/numbers.txt', encoding='utf-8') as f:
    result = (sum(map(int, line.split())) for line in list(f))
    print(*result, sep='\n')