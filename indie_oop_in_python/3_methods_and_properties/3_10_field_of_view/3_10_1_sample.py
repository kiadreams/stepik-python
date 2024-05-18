class Container:
    items = []

    def add_item(self, value):
        self.items.append(value)


box1 = Container()
box1.add_item(2)
box1.add_item(4)


box2 = Container()
box2.add_item(5)
box2.add_item(7)
print(box1.items)
print(box2.items)