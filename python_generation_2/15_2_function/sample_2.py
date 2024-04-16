def print_info(name, surname, age, city, *children, **additional_info):
    print(name, surname, age, city)
    print(children)
    print(additional_info)
    print()
    print('Имя:', name)
    print('Фамилия:', surname)
    print('Возраст:', age)
    print('Город проживания:', city)
    if children:
        print('Дети:', ', '.join(children))
    if additional_info:
        print(additional_info)


children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
additional_info = {'height': 163, 'job': 'actress'}

print_info('Меган', 'Фокс', *children, '34', 'Ок-Ридж',
           **additional_info, some='asf')
