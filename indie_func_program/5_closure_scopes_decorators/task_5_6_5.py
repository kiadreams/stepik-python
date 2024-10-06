def calculate(x, y, operation='a'):\

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def division(a, b):
        if not b:
            return 'На ноль делить нельзя!'
        return a / b

    def multiplication(a, b):
        return a * b

    def is_not_defined(a, b):
        return 'Ошибка. Данной операции не существует'

    operations = {
        'a': addition, 's': subtraction, 'd': division, 'm': multiplication
    }

    print(operations.get(operation, is_not_defined)(x, y))
