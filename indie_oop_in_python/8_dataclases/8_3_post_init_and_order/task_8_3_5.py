from dataclasses import dataclass, field


@dataclass(frozen=True)
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Promo:
    code: str
    value: int = field(compare=False, repr=False)
    products: list[Product] = field(default_factory=list, repr=False)


class Cart:
    def __init__(self):
        self.discount = 0
        self.promo_prods: list[Product] = []
        self.products: dict[Product:int] = {}

    def add_product(self, product: Product, count=1):
        self.products[product] = self.products.get(product, 0) + count

    def get_total(self):
        if self.promo_prods:
            total_price = 0
            for p, n in self.products.items():
                if p in self.promo_prods:
                    total_price += p.price * n * (1 - self.discount / 100)
                else:
                    total_price += p.price * n
            return total_price
        else:
            price = sum([p.price * n for p, n in self.products.items()])
            return price * (1 - self.discount / 100.0)

    def apply_discount(self, discount: int) -> None:
        if isinstance(discount, int) and 1 <= discount <= 100:
            self.discount = discount
            self.promo_prods = []
        else:
            raise ValueError("Неправильное значение скидки")

    def apply_promo(self, promo_code: str) -> None:
        if promo_list := [p for p in ACTIVE_PROMO if p.code == promo_code]:
            promo = promo_list.pop()
            if isinstance(promo.value, int) and 1 <= promo.value <= 100:
                print(f"Промокод {promo_code} успешно применился")
                self.promo_prods = promo.products
                self.discount = promo.value
        else:
            print(f"Промокода {promo_code} не существует")


# Проверка работы кода--------------------------------------------------------
book = Product("Книга", 100.0)
usb = Product("Флешка", 50.0)
pen = Product("Ручка", 10.0)

ACTIVE_PROMO = [
    Promo("new", 20, [pen]),
    Promo("all_goods", 30),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print(cart.get_total())

# Применение промокода в 20% на ручку
cart.apply_promo("new")
print(cart.get_total())

print()
book = Product("Книга", 100.0)
usb = Product("Флешка", 50.0)
pen = Product("Ручка", 10.0)

ACTIVE_PROMO = [
    Promo("new", 20, [pen]),
    Promo("all_goods", 30),
    Promo("only_book", 40, [book]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print(cart.get_total())

# Применение промокода в 40% на книгу
cart.apply_promo("only_book")
print(cart.get_total())
