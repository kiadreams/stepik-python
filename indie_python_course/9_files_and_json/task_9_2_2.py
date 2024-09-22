with open('lorem.txt', encoding='utf-8') as f:
    print(len(set([w.lower() for line in f for w in line.split()])))
