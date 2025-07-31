# При операции += python сперва попытается вызвать метод __iadd__ у объекта.
# Если метод __iadd__  у объекта имеется, значит вызывается он. Если метод
# __iadd__ не реализован, то будет вызван метод __add__ для выполнения
# сложения, а затем результат будет присвоен переменной слева от +=

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __iadd__(self, other):
        print('__iadd__')
        if isinstance(other, (int, float)):
            self.balance += other
        return self


b = BankAccount('vanya', 100)
print(id(b), type(b), b.balance)
b += 150
print(id(b), type(b), b.balance)

# Чтобы ваш объект, когда он участвует в операции +=, был изменяемым,
# вам нужно по экземпляру self присваивать новые значения в атрибуты и,
# обязательно, возвращать сам self из метода, чтобы сохранить ссылку на
# объект. Вот взгляните на реализацию метода __iadd__ ниже

# def __iadd__(self, other):
#     if isinstance(other, (int, float)):
#         self.balance += other
#     return self



# Если же вы хотите работать с неизменяемыми объектами, то вам нельзя менять
# состояние экземпляра self. Но вы можете создать новый экземпляр и вернуть
# его качестве результата:

# def __iadd__(self, other):
#     print('__iadd__')
#     if isinstance(other, (int, float)):
#         return BankAccount(self.name, self.balance + other)
#     raise NotImplemented