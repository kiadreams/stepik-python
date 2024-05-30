# __contains__ — это магический метод, который позволяет вам проверить,
# присутствует ли определенное значение в объекте или нет. Метод
# __contains__ возвращает логическое значение True, если элемент
# присутствует в последовательности и имеет значение False в противном случае.
# Метод __contains__ вызывается каждый раз когда объект используется в
# операции поиска включения через оператор in.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.marks = age

    def __contains__(self, item):
        return item in self.marks


john = Student("John", [5, 4, 5, 3, 4])
print(5 in john)
print(2 in john)
