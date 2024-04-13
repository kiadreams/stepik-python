from random import sample

numbers = sample(range(1, 76), 25)
card = [[str(numbers[i * 5 + j]).ljust(2) for i in range(5)] for j in range(5)]
card[2][2] = '0'.ljust(2)
for elem in card:
    print(*elem)
