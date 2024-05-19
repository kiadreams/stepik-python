class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


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


class Cart:

    def __init__(self, user: User):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product: Product, quantity=1):
        new_quantity = self.goods.get(product, 0) + quantity
        self.goods[product] = new_quantity
        self.__total += product.price * quantity

    def remove(self, product: Product, quantity=1):
        if self.goods.get(product, 0) > quantity:
            self.goods[product] = self.goods.get(product, 0) - quantity
        else:
            quantity = self.goods.pop(product, 0)
        self.__total -= product.price * quantity

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        products = sorted(self.goods.items(), key=lambda prod: prod[0].name)
        for prd, quant in products:
            print(prd.name, prd.price, quant, prd.price * quant)
        print(f"---Total: {self.total}---")


if __name__ == "__main__":
    billy = User("billy@rambler.ru")

    lemon = Product("lemon", 20)
    carrot = Product("carrot", 30)

    cart_billy = Cart(billy)
    print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
    cart_billy.add(lemon, 2)
    cart_billy.add(carrot)
    cart_billy.print_check()
    # """ Печатает текст ниже
    # ---Your check---
    # carrot 30 1 30
    # lemon 20 2 40
    # ---Total: 70---"""
    cart_billy.add(lemon, 3)
    cart_billy.print_check()
    # """ Печатает текст ниже
    # ---Your check---
    # carrot 30 1 30
    # lemon 20 5 100
    # ---Total: 130---"""
    cart_billy.remove(lemon, 6)
    cart_billy.print_check()
    # """ Печатает текст ниже
    # ---Your check---
    # carrot 30 1 30
    # ---Total: 30---"""
    print(cart_billy.total)  # 30
    cart_billy.add(lemon, 5)
    cart_billy.print_check()
    # """ Печатает текст ниже
    # ---Your check---
    # carrot 30 1 30
    # lemon 20 5 100
    # ---Total: 130---"""
    cart_billy.order()
    # """ Печатает текст ниже
    # Не хватает средств на балансе. Пополните счет
    # Проблема с оплатой"""
    cart_billy.user.deposit(150)
    cart_billy.order()  # Заказ оплачен
    print(cart_billy.user.balance)  # 20
