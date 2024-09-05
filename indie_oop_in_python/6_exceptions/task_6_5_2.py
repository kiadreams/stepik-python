class NegativeDepositError(Exception):
    """My first class of exception."""


class InsufficientFundsError(Exception):
    """My second class of exception."""


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError(
                "Нельзя пополнить счет отрицательным значением",
            )
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            raise InsufficientFundsError(
                "Недостаточно средств для снятия",
            )
        self.balance -= value
