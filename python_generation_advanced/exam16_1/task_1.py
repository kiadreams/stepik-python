def generate_letter_2(mail, name, date, time, place,
                    teacher='Тимур Гуев', number=17):
    text = (
        f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!')
    return text




print(generate_letter_2('lara@yandex.ru', 'Лариса', '10 декабря',
                      '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter_2('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))

print()

def generate_letter(mail, name, date, time, place,
                      teacher='Тимур Гуев', number=17):
    text = []
    text.append(f'To: {mail}')
    text.append(f'Приветствую, {name}!')
    text.append(f'Вам назначен экзамен, который пройдет {date}, в {time}.')
    text.append(f'По адресу: {place}.')
    text.append(f'Экзамен будет проводить {teacher} в кабинете {number}.')
    text.append(f'Желаем удачи на экзамене!')
    return '\n'.join(text)


print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря',
                      '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))

print()
a = generate_letter('lara@yandex.ru', 'Лариса', '10 декабря',
                    '12:00', 'Часова 23, корпус 2')
b = generate_letter_2('lara@yandex.ru', 'Лариса', '10 декабря',
                    '12:00', 'Часова 23, корпус 2')
print(a == b)