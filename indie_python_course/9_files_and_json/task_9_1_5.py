with open('numbers.txt', encoding='utf-8') as f:
    data = f.read().split()
    count_nums = sum(1 for n in data if len(n) == 3)
    sum_nums = sum(int(n) for n in data if len(n) == 2)
print(count_nums, sum_nums)