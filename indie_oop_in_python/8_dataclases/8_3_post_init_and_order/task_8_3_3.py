from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float = field(repr=False)


class Cart:

    def __init__(self):
        self.__discount = 0
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total(self):
        total_price = sum([i.price for i in self.products])
        return total_price - (total_price * self.__discount / 100.0)

    def apply_discount(self, discount: int):
        if discount < 1 or discount > 100:
            raise ValueError('Неправильное значение скидки')
        self.__discount = discount


# Проверка работы кода--------------------------------------------------------
product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print(f"Стоимость товаров в корзине без скидки: {cart.get_total()}")
# Применение скидки 10%
cart.apply_discount(10)
print(f"Стоимость товаров в корзине со скидкой 10%: {cart.get_total()}")
print()

product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение скидки 200%
try:
    cart.apply_discount(200)
except ValueError as e:
    print(e)
print(cart.get_total())
