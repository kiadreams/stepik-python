password = input()
if answer := len(password) >= 7:
    for some_func in [str.isdigit, str.isupper, str.islower]:
        answer &= any(map(some_func, password))
print('YES' if answer else 'NO')
