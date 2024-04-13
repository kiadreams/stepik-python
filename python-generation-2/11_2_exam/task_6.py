data_files, actions = {}, dict(write='W', read='R', execute='X')

for _ in range(int(input())):
    file, *l_actions = input().split()
    data_files[file] = l_actions

for _ in range(int(input())):
    action, file = input().split()
    print('OK' if actions[action] in data_files[file] else 'Access denied')