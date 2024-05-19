class Person:

    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in {"male", "female"}:
            self.__gender = gender
        else:
            print("Не знаю, что вы имели в виду? Пусть это будет мальчик!")
            self.__gender = "male"

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        return f"Гражданка {self.surname} {self.name}"
