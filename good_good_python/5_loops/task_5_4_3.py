# operation, num, result = '+', '', 0
# for i in input():
#     if i == ' ':
#         continue
#     elif i.isdigit():
#         num += i
#     elif i in ('+', '-'):
#         result += int(num) if operation == '+' else -int(num)
#         operation, num = i, ''
# result += int(num) if operation == '+' else -int(num)
# print(result)

# Второй вариант...
text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))