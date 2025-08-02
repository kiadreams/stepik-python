from dataclasses import dataclass, field


"""
    При создании класса данных ранее упоминалось, что сперва в классе 
определяются все обязательные атрибуты, и только после них описываются атрибуты
со значениями по умолчанию.
    Следовательно, если родительский класс данных имеет значения по 
    умолчанию для одного или нескольких полей, то ВСЕ поля в подклассе также
    должны иметь значения по умолчанию.
"""



@dataclass
class Person:
    first_name: str
    last_name: str
    age: int = field(default=20)


@dataclass
class Student(Person):
    # course: int  # Ошибка, т.к. все поля должны быть по умолчанию
    course: int = 1
    stipend: int = 1000


mia = Student('Mia', 'Gray', 19, 5, 500)
print(mia)