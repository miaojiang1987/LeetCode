class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        if n==0:
            return 
        self.n = n
        self.row_count = [[0 for i in range(n)] for p in range(2)]
        self.col_count = [[0 for i in range(n)] for p in range(2)]
        self.diag_count = [0 for p in range(2)]
        self.rev_diag_count = [0 for p in range(2)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.row_count[player-1][row]+=1
        self.col_count[player-1][col]+=1
        if row==col:
            self.diag_count[player-1]+=1
        if (row + col) == self.n - 1:
             self.rev_diag_count[player -1] += 1
        if (self.row_count[player-1][row] == self.n or \
        self.col_count[player-1][col] == self.n or \
        self.diag_count[player-1] == self.n or \
        self.rev_diag_count[player-1] == self.n):
            return player
        return 0
        