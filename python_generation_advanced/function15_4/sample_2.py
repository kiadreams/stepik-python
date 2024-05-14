def start():
    # тело функции start
    print('работает функция старта')


def stop():
    # тело функции stop
    print('работает функция стопа')


def pause():
    # тело функции pause
    print('работает функция паузы')


# словарь соответствия команда → функция
commands = {'start': start, 'stop': stop, 'pause': pause}
command = input()  # считываем название команды
commands[command]()  # вызываем нужную функцию через словарь по ключу
