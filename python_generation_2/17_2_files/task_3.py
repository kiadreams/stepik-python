import random


f = open('lines.txt', encoding='utf-8')
print(random.choice(f.readlines()).rstrip())
f.close()