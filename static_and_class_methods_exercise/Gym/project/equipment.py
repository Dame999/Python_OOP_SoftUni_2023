class Equipment:
    ID_NUMBER = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

        self.ID_NUMBER += 1

    @staticmethod
    def get_next_id():
        return Equipment.ID_NUMBER

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
