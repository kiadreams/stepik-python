class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    def deposit(self, money):
        self.__balance += money

    def is_money_enough(self, money):
        return self.__balance >= money

    def payment(self, money):
        if self.is_money_enough(money):
            self.__balance -= money
            return True
        print("Не хватает средств на балансе. Пополните счет")
        return False
