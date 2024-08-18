class Voter:
    def __init__(self, id, name):
        self.id = id
        self.name:str = name

    def __repr__(self):
        return f"{self.id} -> {self.name}"