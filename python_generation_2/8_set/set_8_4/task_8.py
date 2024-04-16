string_1, string_2 = (input() for _ in range(2))
result = ('NO', 'YES')[set(string_1) == set(string_2)]
print(result)