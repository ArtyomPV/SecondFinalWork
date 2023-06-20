import Note


class Notebook:
    user_id =1

    def __init__(self, path: str = 'notes.txt'):
        self.path = path
        self.notes: dict[int:Note] = {}
        self.uid = Notebook.user_id
        Notebook.user_id += 1


    def add(self, newNote: Note):
        self.notes[newNote.uid] = newNote


# notebook = Notebook()
# notebook.add(note('title1', 'message1'))
