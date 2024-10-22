def is_member(a, l):
    if not l:
        return False
    elif a == l[0]:
        return True
    else:
        return is_member(a, l[1:])


print(is_member("e", ['a', 'e', 'i', 'o', 'u']))