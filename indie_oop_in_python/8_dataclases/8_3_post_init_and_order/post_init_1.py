from dataclasses import dataclass, field


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int = field(default=20)
    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = f'{self.first_name} {self.last_name}'
        self.is_programmer = True


artem = Person('Artem', 'Egorov')
print(artem)
print(artem.__dict__)
