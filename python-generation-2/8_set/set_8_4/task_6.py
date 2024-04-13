string = input()
result = ['NO', 'YES'][len(string) == len(set(string))]
print(result)
