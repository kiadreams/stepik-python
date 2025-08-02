from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Promo:
    code: str
    value: int = field(compare=False, repr=False)


class Cart:

    def __init__(self):
        self.discount = 0
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total(self):
        total_price = sum([i.price for i in self.products])
        return total_price - (total_price * self.discount / 100.0)

    def apply_discount(self, discount: int) -> None:
        if isinstance(discount, int) and 1 <= discount <= 100:
            self.discount = discount
        else:
            raise ValueError('Неправильное значение скидки')

    def apply_promo(self, promo_code: str) -> None:
        promo_list = [p for p in ACTIVE_PROMO if p.code == promo_code]
        if promo_list:
            value = promo_list.pop().value
            if isinstance(value, int) and 1 <= value <= 100:
                self.discount = value
                print(f'Промокод {promo_code} успешно применился')
        else:
            print(f'Промокода {promo_code} не существует')


# Проверка работы кода--------------------------------------------------------
ACTIVE_PROMO = [
    Promo('new', 20),
    Promo('all_goods', 30),
]

product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение промокода в 30%
cart.apply_promo('all_goods')
print(cart.get_total())
