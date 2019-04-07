import re
from collections import defaultdict


class Claim(object):
    def __init__(self, claim: str):
        params = re.findall('#(\d+)\s@ (\d+),(\d+):\s(\d+)x(\d+)', claim)[0]
        self.id, self.x, self.y, self.width, self.height = map(int, params)

    def __repr__(self):
        return f'Claim: <id: {self.id}, x: {self.x}, y: {self.y}, w:{self.width}, h:{self.height}>\n'


class Board(object):
    def __init__(self):
        self.board = defaultdict(lambda: defaultdict(list))

    def __repr__(self):
        return str(self.board)

    def __getitem__(self, item):
        return self.board[item]

    def add_claim(self, claim: Claim):
        for x in range(claim.x, claim.x + claim.width):
            for y in range(claim.y, claim.y + claim.height):
                self.board[x][y].append(claim.id)


def main():
    """
    >>> main()
    """
    with open('input-3.txt') as f:
        board = Board()
        claims = [Claim(line) for line in f]
        for claim in claims:
            board.add_claim(claim)
    counter = 0
    single_claims = set()
    non_single_claims = set()
    for x in range(1000):
        for y in range(1000):

            if len(board[x][y]) > 1:
                counter += 1
                non_single_claims = non_single_claims.union(set(board[x][y]))
            elif len(board[x][y]) == 1:
                single_claims.add(board[x][y][0])
    print(counter)
    print(single_claims.difference(non_single_claims))
