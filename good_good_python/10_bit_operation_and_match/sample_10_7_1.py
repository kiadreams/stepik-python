CMD_3 = 3 # Просто в константы из этого же модуля в MATCH использовать
# нельзя!!!
CMD_5 = 5

class Const:

    C_CMD_7 = 7
    C_CMD_8 = 8


cmd = 7

match cmd:
    case int() as value_cmd if value_cmd == CMD_3:
        print(f'{cmd=}')
    case Const.C_CMD_7:
        print(f'{cmd=}')
    case 5:
        print(f'{cmd=}')