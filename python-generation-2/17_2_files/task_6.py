f = open('prices.txt', encoding='utf-8')
prices = [line.split() for line in f.readlines()]
f.close()
print(sum([int(q) * int(p) for _, q, p in prices]))

