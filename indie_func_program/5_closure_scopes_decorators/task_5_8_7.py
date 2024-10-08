def create_dict():
    count = 0
    calls = {}

    def _inner(s):
        nonlocal count
        count += 1
        calls[count] = s
        return calls

    return  _inner

f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))