# В базовом курсе мы познакомились с type,  но там я назвал его функцией.
# Пора исправить это недоразумение и официально заявить, что type является
# классом.

# Класс type может использоваться для двух целей:
#  1. определение типа объекта
#  2. создание нового типа или класс

# Вызов type(instance) возвращает класс, от которого был создан экземпляр.
# Для каждого экземпляра будет возвращаться именно тот класс, от которого он
# был создан:


class Person:
    pass


class Doctor(Person):
    pass


class Teacher(Person):
    pass


p = Person()
d = Doctor()
t = Teacher()

print(type(p))
print(type(d))
print(type(t))
print()

# Результат вызова type можно использовать в проверках для определения
# принадлежности экземпляра к конкретному классу. Такая проверка может
# пригодиться для вызова метода, который есть только в определенном классе.


class Person:
    def can_sleep(self):
        print("Я могу спать")

    def can_walk(self):
        print("Я могу ходить")


class Doctor(Person):
    def can_cure(self):
        print("Я могу лечить")


items = [Person(), Doctor()]
for instance in items:
    if type(instance) is Doctor:
        instance.can_cure()

# Если передавать сам класс и затем вызывать type(class), результатом всегда
# будет type. Почему? Ответ в разделе «Метапрограммирование».

print(type(Doctor))  # результатом всегда будет type
