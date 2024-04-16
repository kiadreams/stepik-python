# from functools import reduce

words = [input() for _ in range(int(input()))]
result = sorted(words, key=lambda w: (sum(ord(x) - 65 for x in w.upper()), w))
# key=lambda x: (reduce(lambda a, x: a + ord(x) - 65, x.upper(), 0), x))
print(*result, sep='\n')
