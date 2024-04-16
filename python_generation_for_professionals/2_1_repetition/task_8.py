# Вариант мой...
# def index_of_nearest(numbers: [int], number: int) -> int:
#     answer = -1
#     if numbers:
#         number_list = [(ind, abs(number - value))
#                        for ind, value in enumerate(numbers)]
#         answer = sorted(number_list, key=lambda x: (x[1], x[0]))[0][0]
#     return answer

# Вариант с подсказкой преподавателя...
def index_of_nearest(numbers: list[int], number: int) -> int:
    answer = -1
    if numbers:
        min_change = min(numbers, key=lambda x: abs(x - number))
        answer = numbers.index(min_change)
    return answer


print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
