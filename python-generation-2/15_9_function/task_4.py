some_ip = input().split('.')
result = all(
    map(lambda x: 0 <= int(x) <= 255 if x.isdigit() else False, some_ip)
)
print(result)