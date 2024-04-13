f = open('nums.txt', encoding='utf-8')
print(sum([int(num) for num in f.read().split()]))
f.close()
