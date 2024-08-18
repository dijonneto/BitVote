import hashlib
from entities.vote import Vote

class Block:
    def __init__(self, index, previous_hash, vote, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.vote:Vote = vote
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.vote}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()