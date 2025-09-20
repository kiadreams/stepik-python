from collections import Counter
from typing import Optional


def find_majority_element(nums: list) -> Optional[int]:
    if nums:
        el, count = Counter(nums).most_common(1)[0]
        return el if count > len(nums) // 2 else None
    return None


assert find_majority_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]) == 3

# Тест 2: Элемент большинства присутствует
assert find_majority_element([6, 8, 4, 6, 8, 6, 6]) == 6

# Тест 3: Элемент большинства отсутствует
assert find_majority_element([1, 2, 3]) is None

# Тест 4: Пустой список
assert find_majority_element([]) is None

# Тест 5: Список с одним элементом
assert find_majority_element([7]) == 7

# Тест 6: Список с двумя элементами
assert find_majority_element([7, 7]) == 7

# Тест 7: Список с тремя элементами (элемент большинства отсутствует)
assert find_majority_element([7, 8, 9]) is None