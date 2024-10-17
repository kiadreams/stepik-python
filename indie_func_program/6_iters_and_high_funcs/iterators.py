from sys import getsizeof


numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(tuple(iterator))
print(list(iterator))

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(sum(iterator))
print(sum(iterator))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 45, '234', 'qer', 23342, '234']
iterator = iter(numbers)

print(getsizeof(numbers), getsizeof(iterator), f'длина колекции: {len(numbers)}')


too_much_numbers = list(range(1000000))
iterator = iter(too_much_numbers)

print(getsizeof(too_much_numbers), getsizeof(iterator ), f'длина колекции: {len(too_much_numbers)}')
