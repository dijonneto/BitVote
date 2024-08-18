import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", None, time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def add_vote(self, encrypted_vote):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, encrypted_vote, time.time())
        self.add_block(new_block)

    def validate_vote(self, voter_id):
        for block in self.chain:
            for vote in block.votes:
                if vote.voter_id == voter_id:
                    return False  # Voto já registrado
        return True