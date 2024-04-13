names_1 = {number for number in input().split()}
names_2 = {number for number in input().split()}
print(*sorted(names_1 | names_2))
