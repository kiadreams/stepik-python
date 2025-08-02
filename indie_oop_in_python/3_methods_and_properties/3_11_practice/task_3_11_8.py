class Pizza:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def peperoni(cls):
        return cls(["mozzarella", "peperoni", "tomatoes"])

    @classmethod
    def barbecue(cls):
        return cls(["mozzarella", "red onion", "sauce bbq", "chicken"])


# Провекра работы------------------------------------------------------------
# Тест №1
bbq = Pizza.barbecue()
peperoni = Pizza.peperoni()
margherita = Pizza.margherita()
assert sorted(bbq.ingredients) == ["chicken", "mozzarella", "red onion", "sauce bbq"]
assert sorted(peperoni.ingredients) == ["mozzarella", "peperoni", "tomatoes"]
assert sorted(margherita.ingredients) == ["mozzarella", "tomatoes"]
