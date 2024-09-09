from typing import Protocol


class Animal(Protocol):
    def walk(self) -> None: ...

    def speak(self) -> None: ...


class Dog:

    def __init__(self, name):
        self.name = name

    def walk(self) -> None:
        print("This is a dog walking")

    def speak(self) -> None:
        print(f"{self.name}: Woof!")


def make_animal_speak(animal: Animal) -> None:
    animal.speak()


dog = Dog('Sharic')
make_animal_speak(dog)
