# 1 вариант мой...
# def get_names(all_name: str) -> tuple:
#     name = ''.join([i for i in all_name if not i.isdigit()])
#     return name, all_name

# def crt_unique_name(name: str, names: list) -> str:
#     count, all_name = 1, name
#     while all_name in names:
#         all_name = f'{name}{count}'
#         count += 1
#     return all_name

# num_people, postfix = {}, '@beegeek.bzz'
# for _ in range(int(input())):
#     name, all_name = get_names(input().split('@')[0])
#     num_people.setdefault(name, []).append(all_name)
# for _ in range(int(input())):
#     name, all_name = get_names(input())
#     if all_name in num_people.setdefault(name, []):
#         all_name = crt_unique_name(name, num_people[name])
#     print(f'{all_name}{postfix}')
#     num_people.get(name, []).append(all_name)

# Проще..

all_email = {input() for _ in range(int(input()))}
for _ in range(int(input())):
    name = input()
    email = f'{name}@beegeek.bzz'
    count = 1
    while email in all_email:
        email = name.rstrip('1234567890') + f'{count}@beegeek.bzz'
        count += 1
    all_email.add(email)
    print(email)
        
