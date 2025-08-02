import random
import string
from dataclasses import dataclass, field


alphabet = string.ascii_uppercase + string.digits


def generate_guid():
    guid = ''.join(random.choices(alphabet, k=15))
    return guid


@dataclass(order=True)
class Student:
    sort_index: tuple = field(init=False, repr=False)
    first_name: str
    last_name: str
    guid: str = field(init=False, repr=False)
    email: str = field(init=False)
    tuition: float = field(default=0, repr=False)

    def __post_init__(self):
        self.sort_index = (self.tuition, self.last_name, self.first_name)
        self.guid = generate_guid()
        self.email = f'{self.first_name}.{self.last_name}@uni.edu'.lower()


# Проверка работы кода--------------------------------------------------------
jane = Student('Jane', 'Lee', 30000)
julia = Student('Julia', 'Doe', 10000)
jake = Student('Jake', 'Langdon', 20000)
joy = Student('Joy', 'Smith', 15000)
print(*sorted([jane, julia, jake, joy]), sep='\n')
