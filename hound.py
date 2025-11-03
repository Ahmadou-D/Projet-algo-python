
class Hound:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def canMoveTo(self, board, row, col):
        size = board.size
        if row < 0 or row >= size or col < 0 or col >= size:
            return False
        if board.get(row, col) != 0:
            return False

        return (row == self.row + 1 and abs(col - self.col) == 1)

    def canMove(self, board):
        moves = [(self.row + 1, self.col - 1), (self.row + 1, self.col + 1)]
        return any(self.canMoveTo(board, r, c) for r, c in moves if 0 <= r < board.size and 0 <= c < board.size)

