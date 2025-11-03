# Ahmadou Diallo et Aleksandar Lakic

from hound import Hound

class Fox(Hound):
    def canMoveTo(self, board, row, col):
        size = board.size
        if row < 0 or row >= size or col < 0 or col >= size:
            return False
        if board.get(row, col) != 0:
            return False

        return abs(row - self.row) == 1 and abs(col - self.col) == 1

    def win(self):
        return self.row == 0
