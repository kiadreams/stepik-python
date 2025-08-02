from dataclasses import dataclass, field

"""
    Чтобы обеспечить порядок среди экземпляров класса данных и впоследствии 
отсортировать их на основе определенного атрибута в классе данных, 
вам следует установить параметр order в значение True в декораторе 
@dataclass и определить дополнительный атрибут sort_index (в качестве 
имени вы можете выбрать другое значение).

    Вы можете добавить поле sort_index в класс данных. И вам стоит выполнить 
следующие рекомендации:
    - sort_index должен определиться самым первым атрибутом, чтобы он стоял 
      к кортеже сравнения спереди и по нему выполнялось сравнение в первую 
      очередь
    - Пользователям не нужно инициализировать sort_index, поэтому установите 
      для init значение False в функции field.
    - Вы также можете исключить поле из строки представления, установив для 
      repr значение False.
    - в методе __post_init__ определите значение, которое пойдет в поле 
      sort_index
"""


@dataclass(order=True)
class Person:
    sort_index1: int | tuple = field(init=False, repr=False)
    name: str
    age: int
    weight: int = 190

    def __post_init__(self):
        # pass
        # self.sort_index1 = self.weight
        self.sort_index1 = (self.weight, self.age)


persons = [
    Person('Иван', 25, 200),
    Person('Петр', 30, 150),
    Person('Кирилл', 35, 150),
    Person('Борис', 20, 200),
    Person('Алексей', 15, 200),
    Person('Дмитрий', 11, 175),

]

print(*sorted(persons), sep='\n')
