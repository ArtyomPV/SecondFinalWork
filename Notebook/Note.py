class Note:
    user_id = 1

    def __init__(self, title, message):
        self.time = 'time'
        self.title = 'title'
        self.message = 'message'
        self.uid = Note.user_id
        Note.user_id += 1

    def __str__(self):
        return f'id: {self.uid}\ntitle: {self.title}\nmessage: {self.message}'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


note1 = Note()
note2 = Note()
print(note1)
print(note2)