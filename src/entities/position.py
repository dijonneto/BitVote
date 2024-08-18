from entities.candidate import Candidate

class Position:
    def __init__(self, title):
        self.title:str = title
        self.candidates:list[Candidate] = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def __repr__(self):
        return f"Position(Title: {self.title}, Candidates: {[candidate.name for candidate in self.candidates]})"
