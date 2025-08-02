class StringValidation:

    def __set_name__(self, owner, name):
        print(f'__set_name__ called: owner={owner}, attr_name={name}')
        self.attribute_name = '_' + name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        key = self.attribute_name
        return getattr(instance, key, None)

    def __set__(self, instance, value):
        key = self.attribute_name
        setattr(instance, key, value)


class Person:
    name = StringValidation()
    last_name = StringValidation()


p = Person()
p.name = 'Alex'
p.last_name = 'Sidorov'
print(p.name, p.last_name)  # Alex Sidorov
print(p.__dict__)  # {'_name': 'Alex', '_last_name': 'Sidorov'}