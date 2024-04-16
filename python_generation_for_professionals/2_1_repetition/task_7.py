def likes(names: list) -> str:
    res_string = 'Никто не оценил'
    if len(names) == 1:
        res_string = f'{names[0]} оценил(а)'
    elif len(names) == 2:
        res_string = f'{names[0]} и {names[1]} оценили'
    elif len(names) > 2:
        text = names[2] if len(names) == 3 else f'{len(names) - 2} других'
        res_string = f'{names[0]}, {names[1]} и {text} оценили'
    return res_string + ' данную запись'


print(likes(['Дима', 'Алиса']))
print(likes(['Эндрю', 'Тоби', 'Том']))
print(likes([]))
