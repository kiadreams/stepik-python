class InfinityIterator:
    def __init__(self, start=0):
        self.start = start
        self.d = 10

    def __iter__(self):
        return self

    def __next__(self):
        num = self.start
        self.start += self.d
        return num


# Проверка работы класса------------------------------------------------------
nums = []
for i in InfinityIterator(1):
    nums.append(i)
    if len(nums) == 5:
        break
assert nums == [1, 11, 21, 31, 41]