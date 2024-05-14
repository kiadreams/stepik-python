number, schoolboys = int(input()), []
schoolboys = [input().split() for _ in range(number)]
schoolboys = [(name, int(score)) for name, score in schoolboys]
for person in schoolboys:
    print(*person)
print()
for person in schoolboys:
    if person[1] > 3:
        print(*person)

# Как вариант
    
# m = tuple([input() for _ in range(int(input()))])
# print(*m, '', *filter(lambda pair: pair[-1] > '3', m), sep='\n')
