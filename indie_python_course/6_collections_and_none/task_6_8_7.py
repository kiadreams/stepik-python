def get_dict(ls: list) -> dict | None:
    if len(ls) == 2:
        return {ls[0]: ls[1]}
    elif len(ls) > 2:
        return {ls[0]: get_dict(ls[1:])}
    else:
        return None


print(get_dict([int(i) for i in input().split()]))
