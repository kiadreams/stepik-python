def pretty_print(data, side='-', delimiter='|'):
    data = [str(item) for item in data]
    some_delim = ' ' + delimiter + ' '
    line = [side * (len(item) + 2) for item in data]
    line.append(side * (len(data) - 1))
    out_line = some_delim.join(data)
    print(' ' + ''.join(line))
    print(f'{delimiter} {out_line} {delimiter}')
    print(' ' + ''.join(line))


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# Вариант №2
def pretty_print_2(data, side='-', delimeter='|'):
    line = f" {delimeter} ".join(map(str, data))
    print(' ' + side * (2 + len(line)))
    print(delimeter + ' ' + line + ' ' + delimeter)
    print(' ' + side * (2 + len(line)))
