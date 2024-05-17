class Notebook:

    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for i, note in enumerate(self._notes):
            print(f"{i + 1}.{note}")


note = Notebook(["Buy Potato", "Buy Carrot", "Wash car"])
note.notes_list
