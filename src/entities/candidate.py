from entities.party import Party
from entities.position import Position

# Definição das classes para Cargos e Candidatos
class Candidate:
    def __init__(self, name, party, position):
        self.name:str = name
        self.party:Party = party
        self.position:Position = position

    def __repr__(self):
        return f"Candidate(Name: {self.name}, Party: {self.party}, Position: {self.position})"