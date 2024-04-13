all_numbers = input() + input()
result = ('NO', 'YES')[len(set(all_numbers)) == 10]
print(result)