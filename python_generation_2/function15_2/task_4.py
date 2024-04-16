def greet(name, *args):
    names = ' and '.join((name,) + args)
    return f'Hello, {names}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
