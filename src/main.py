from block import Block
from blockchain import Blockchain
from entities.position import Position
from entities.candidate import Candidate
from entities.vote import Vote
from entities.voter import Voter
from entities.party import Party

def main():
  # Simulação de uma eleição
  blockchain = Blockchain()

  # Definição de cargos
  president_position = Position("President")
  governor_position = Position("Governor")

  # Definição de partidos
  party1 = Party("1", "Party 1")
  party2 = Party("2", "Party 2")
  party3 = Party("3", "Party 3")

  # Adição de candidatos
  candidate1 = Candidate("Alice", party1, president_position)
  candidate2 = Candidate("Bob", party2, president_position)
  candidate3 = Candidate("Charlie", party3, governor_position)

  president_position.add_candidate(candidate1)
  president_position.add_candidate(candidate2)
  governor_position.add_candidate(candidate3)

  voter1 = Voter("1", "voter1")
  voter2 = Voter("2", "voter2")
  voter3 = Voter("3", "voter3")

  vote1 = Vote(voter1, candidate1)
  vote2 = Vote(voter2, candidate2)
  vote3 = Vote(voter3, candidate3)

  # Registro de votos
  blockchain.add_vote(vote1)
  blockchain.add_vote(vote2)
  blockchain.add_vote(vote3)

  # Visualizar os votos registrados
  block: Block
  for block in blockchain.chain[1:]:
      print(f"Block {block.index} [Hash: {block.hash}]")
      print(f"Voter ID: {block.vote.voter.id} | Name: {block.vote.voter.name}")
      print(f"Position: {block.vote.candidate.position}")
      print(f"Candidate: {block.vote.candidate.name}")
      print("-" * 30)

if __name__ == "__main__":
    main()