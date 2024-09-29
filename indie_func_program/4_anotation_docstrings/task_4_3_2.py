def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    """Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"""
    new_list = lst[:]
    if shift < 0:
        new_list.reverse()
    for i in range(abs(shift)):
        el = new_list.pop()
        new_list.insert(0, el)
    if shift < 0:
        new_list.reverse()
    return new_list


nums = [1, 2, 3, 4]
new_nums = rotate(nums)
print(nums)
print(new_nums)

print()

print(rotate([1, 2, 3, 4, 5, 6], 2))

print()

print(rotate([1, 2, 3, 4, 5, 6], 0))
print(rotate([6, 5, 4, 3, 2, 1], -1))