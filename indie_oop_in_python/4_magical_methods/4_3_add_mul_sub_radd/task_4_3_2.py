# Напишите определение класса Order
class Order:

    def __init__(self, cart: list, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            new_cart = self.cart.copy()
            new_cart.remove(other)
        else:
            new_cart = self.cart
        return Order(new_cart, self.customer)

    def __rsub__(self, other):
        return self.__sub__(other)

# Ниже код для проверки методов класса Order

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')