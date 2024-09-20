users = {}
for _ in range(int(input())):
    name = input()
    if name in users:
        cnt = users.get(name) + 1
        new_name = name + str(cnt)
        users[name] = cnt
        users[new_name] = 0
        print(new_name)
    else:
        users[name] = 0
        print('OK')
