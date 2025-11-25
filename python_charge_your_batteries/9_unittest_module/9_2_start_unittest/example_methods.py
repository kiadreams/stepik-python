from typing import Optional


def calculate_average(numbers: list) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_reading_time(self):
        return f"{self.pages * 1.5} minutes"

    def apply_discount(self, discount):
        if not isinstance(discount, float):
            raise ValueError('Discount must be float number')
        if 0 <= discount <= 1:
            discounted_price = self.price - (discount * self.price)
            return f"${discounted_price}"
        raise ValueError('Discount must be float number between 0 and 1')
