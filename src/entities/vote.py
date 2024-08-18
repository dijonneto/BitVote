from entities.voter import Voter
from entities.candidate import Candidate
import time

class Vote:
    def __init__(self, voter, candidate):
        self.voter:Voter = voter
        self.candidate:Candidate = candidate
        self.timestamp = time.time()

    def __repr__(self):
        return f"{self.voter} -> {self.candidate} @ {self.timestamp}"