numbers_1 = {int(number) for number in input().split()}
numbers_2 = {int(number) for number in input().split()}
if numbers_1.isdisjoint(numbers_2):
    print('BAD DAY')
else:
    print(*sorted((numbers_2 & numbers_1), reverse=True))
