class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.weight}г."


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def __str__(self):
        sort_ingredient = sorted(
            self.ingredients,
            key=lambda i: i.weight,
            reverse=True
        )
        str_ingredients = '\n'.join(map(str, sort_ingredient))
        return f'Пицца {self.name} состоит из:\n' + str_ingredients


# Проверка работы-------------------------------------------------------------
# Тест №1
barbecue = Pizza(
    "BBQ",
    [
        Ingredient("chicken", 200),
        Ingredient("mozzarella", 300),
        Ingredient("sauce bbq", 150),
        Ingredient("red onion", 150),
    ],
)

t = '''
Пицца BBQ состоит из:
mozzarella: 300г.
chicken: 200г.
sauce bbq: 150г.
red onion: 150г.
'''

assert str(barbecue) == t.strip()

# Тест №2
tomatoes = Ingredient('tomatoes', 200)
cheese = Ingredient('mozzarella', 400)
assert str(tomatoes) == 'tomatoes: 200г.'
assert str(cheese) == 'mozzarella: 400г.'

peperoni = Pizza('Пеперони')
peperoni.ingredients.append(tomatoes)
peperoni.ingredients.append(cheese)

t = '''
Пицца Пеперони состоит из:
mozzarella: 400г.
tomatoes: 200г.
'''
assert str(peperoni) == t.strip()