def find_keys(**kwargs):
    names = [k for k, v in kwargs.items() if isinstance(v, (list, tuple))]
    print(names)
    return names


print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))