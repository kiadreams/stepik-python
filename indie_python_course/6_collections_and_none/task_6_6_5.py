numbers = [int(x) for x in input().split()]
my_dict = {numbers.pop(-2): numbers.pop()}
while numbers:
    my_dict = {numbers.pop(): my_dict}
print(my_dict)
