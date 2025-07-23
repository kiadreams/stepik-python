class MaxLengthAttribute:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance.__dict__:
            return sorted(
                instance.__dict__.keys(),
                key=lambda x: (len(x), x.lower()),
            ).pop()
        else:
            return None


class Dog:
    max_length_atr = MaxLengthAttribute()


d = Dog()
d.name = 'dddd'
d.cats = 'aaaa'
print(d.max_length_atr)
