# Ahmadou Diallo

from gameBoard import GameBoard
from hound import Hound
from fox import Fox

class FoxAndHounds:
    def __init__(self, size=8):
        self.board = GameBoard(size)
        self.fox = Fox(size - 1, size // 2)
        self.hounds = [Hound(0, j) for j in range(1, size, 2)]

    def canFoxMove(self):
        for r in [-1, 1]:
            for c in [-1, 1]:
                nr, nc = self.fox.row + r, self.fox.col + c
                if self.fox.canMoveTo(self.board, nr, nc):
                    return True
        return False

    def play(self):
        turn = "fox"
        while True:
            self.board.display()
            if self.fox.win():
                print(" Le renard a gagné !")
                break
            if not self.canFoxMove():
                print(" Les chiens ont gagné !")
                break

            if turn == "fox":
                print("Tour du renard :")
                row = int(input("Nouvelle ligne : ")) - 1
                col = int(input("Nouvelle colonne : ")) - 1
                if self.fox.canMoveTo(self.board, row, col):
                    self.board.set(self.fox.row, self.fox.col, 0)
                    self.fox.row, self.fox.col = row, col
                    self.board.set(row, col, -1)
                    turn = "hound"
                else:
                    print("Déplacement impossible.")
            else:
                print("Tour des chiens :")
                num = int(input("Choisir un chien (1 à {}) : ".format(len(self.hounds))))
                hound = self.hounds[num - 1]
                if not hound.canMove(self.board):
                    print("Ce chien ne peut pas bouger.")
                    continue
                row = int(input("Nouvelle ligne : ")) - 1
                col = int(input("Nouvelle colonne : ")) - 1
                if hound.canMoveTo(self.board, row, col):
                    self.board.set(hound.row, hound.col, 0)
                    hound.row, hound.col = row, col
                    self.board.set(row, col, num)
                    turn = "fox"
                else:
                    print("Déplacement impossible.")

