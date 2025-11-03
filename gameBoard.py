# Ahmadou Diallo

class GameBoard:
    def __init__(self, size):
        if size % 4 != 0:
            size += 4 - (size % 4)
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        # Hounds (lignes du haut)
        num_hound = 1
        for j in range(1, self.size, 2):
            board[0][j] = num_hound
            num_hound += 1
        # Fox (ligne du bas)
        board[self.size - 1][self.size // 2] = -1
        return board

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                val = self.board[i][j]
                if val == 0:
                    print('.', end=' ')
                elif val == -1:
                    print('F', end=' ')
                else:
                    print(val, end=' ')
            print()
        print()

    def get(self, row, col):
        return self.board[row][col]

    def set(self, row, col, value):
        self.board[row][col] = value

