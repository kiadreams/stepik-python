class my_defaultdict(dict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not callable(default_factory) and default_factory is not None:
            raise TypeError('first argument must be callable or None')
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = self.default_factory()
        return self[key]


dd_one = my_defaultdict(list)
print(dd_one)  # {}
dd_one['missing']
print(dd_one)  # {'missing': []}

dd_one.default_factory = int
print(dd_one['another_missing'])  # 0
print(dd_one['another_missing'])  # 0
print(dd_one)  # {'missing': [], 'another_missing': 0}
