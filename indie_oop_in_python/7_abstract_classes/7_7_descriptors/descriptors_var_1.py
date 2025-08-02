class StringValidation:

    def __set_name__(self, owner, name):
        print(f'__set_name__ called: owner={owner}, attr_name={name}')
        self.attribute_name = name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)

    def __set__(self, instance, value):
        print(f'присваевается новое значение {value}')
        instance.__dict__[self.attribute_name] = value


class Person:
    name = StringValidation()
    last_name = StringValidation()


p = Person()
p.name = 'Alex'
p.last_name = 'Sidorov'
print(p.name, p.last_name)  # Alex Sidorov
print(p.__dict__)  # {'name': 'Alex', 'last_name': 'Sidorov'}
print()
p.name = 'Sanya'
p.last_name = 'Popov'
print(p.name, p.last_name)  # Alex Sidorov
print(p.__dict__)  # {'name': 'Alex', 'last_name': 'Sidorov'}