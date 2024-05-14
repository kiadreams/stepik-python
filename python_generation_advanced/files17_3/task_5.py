with open('17_3_files/nums.txt', encoding='utf-8') as f:
        nums = [x if x.isdigit() else ' ' for x  in f.read()]
        result = sum(map(int, ''.join(nums).split()))
print(result)