numbers_1 = {int(number) for number in input().split()}
numbers_2 = {int(number) for number in input().split()}
print(('NO', 'YES')[numbers_2 == numbers_1])
