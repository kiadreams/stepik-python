from dataclasses import dataclass, field


@dataclass(order=True)
class Athlet:
    sort_index: float = field(init=False, repr=False)
    name: str
    coefficient: float = field(repr=False)
    scores: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        self.sort_index = self.coefficient * sum(self.scores) / len(self.scores)


# Проверка работы кода--------------------------------------------------------
sportsmans = [
    Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
    Athlet('Кирилл', 1.6, [9.0, 8.0, 10.0]),
    Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
    Athlet('Аркадий', 1.1, [10.0, 9.5, 8.7]),
    Athlet('Алексей', 1.2, [8.0, 7.0, 6.0]),
    Athlet('Всеволод', 1.5, [8.0, 7.0, 7.0])
]

print("Итоговая таблица")
for i, sportsman in enumerate(sorted(sportsmans, reverse=True)):
    print(f"{i+1}.{sportsman}")