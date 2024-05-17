class MagicalBox:
    def __init__(self, contents=None):
        self._contents = contents

    @property
    def contents(self):
        if self._contents == "rabbit":
            return "🐇 A magical rabbit!"
        else:
            return self._contents

    @contents.setter
    def entity(self, new_contents): # вот тут поменялось название
        if new_contents == "wishes":
            print("🌟 Your wishes are granted!")
            self._contents = new_contents
        else:
            print("✨ The magic didn't work this time.")
            self._contents = new_contents


box = MagicalBox("rubies")
print(f"{box.contents=}, {box.entity=}, {box._contents=}")
try:
    box.contents = 'sdaf'
except AttributeError:
    print("box.contents = 'sdaf' - не работает...")
box.entity = 'присвоили box.entity ='
print(f"{box.contents=}, {box.entity=}, {box._contents=}")


