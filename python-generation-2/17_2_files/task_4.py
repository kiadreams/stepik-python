f = open('numbers.txt', encoding='utf-8')
print(sum(map(int, f.readlines())))
f.close()