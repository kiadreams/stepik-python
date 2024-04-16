#  Вариант №1
def same_parity(numbers):
    return [x for x in numbers if x % 2 == numbers[0] % 2]


#  Вариант №2
# def same_parity(numbers):
#     if numbers:
#         parity = numbers[0] % 2
#         return [x for x in numbers if x % 2 == parity]
#     return numbers
