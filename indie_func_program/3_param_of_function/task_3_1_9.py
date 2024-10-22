def is_dunder(method):
    if len(method) < 6:
        return False
    if method.startswith('__') and method.endswith('__'):
        return method[2:-2].isalpha()
    return False


print(is_dunder('__str__'))
print(is_dunder('___bool___'))
