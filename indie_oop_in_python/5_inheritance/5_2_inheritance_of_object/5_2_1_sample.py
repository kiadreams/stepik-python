# Вы можете создать класс, который будет наследоваться от любого встроенного
# типа. В примере ниже мы создаем класс MyList от списка.
# После этого класс MyList получит поведение класса list,  а значит,
# можно использовать любой метод обычного списка для экземпляров класса MyList


class MyList(list):
    # Если вы добавите новый метод внутри класса MyList, которого не было в
    # классе-родителе list, то тем самым только расширите функционал вашего класса.

    # Например, у списка есть стандартный метод .append(), который добавляет
    # один элемент в конец списка. Мы можем сделать метод double_append(),
    # который будет дважды добавлять элемент в конец списка.

    pass

    # Обратите внимание, что в самой реализации метода.double_append() я дважды
    # вызываю оригинальный метод.append() у самого list
    def double_append(self, value):
        self.append(value)
        self.append(value)


s = MyList()
print(s)
s.append(23)
s.extend((12, 5, 12))
s.insert(0, 200)
print(s)
s.reverse()
print(s)
print()
# Экземпляр класса MyList будет принадлежать как классу MyList ,
# так и классам list и object

print(isinstance(s, MyList))
print(isinstance(s, list))
print(isinstance(s, object))
print()

s = MyList([1, 2, 3])
print(s)
s.append(23)
print(s)
s.double_append(200)
print(s)
s.double_append(555)
print(s)
