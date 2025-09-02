
# считывание списка из входного потока
lst_in = ['название_1=url_1', 'название_2=url_2', 'название_3=url_3']
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

menu = {**menu, **dict([i.split('=') for i in lst_in])}
print(menu)
print(23)
