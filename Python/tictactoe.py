class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        # orders are hor, vert, diag, adiag
        self.rows = [[0]*n, [0]*n]
        self.cols = [[0]*n, [0]*n]
        self.diags = [0,0]
        self.adiags = [0,0]


        
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
        self.rows[player-1][col]+=1
        if self.rows[player-1][col]==self.n: return player
        self.cols[player-1][row]+=1
        if self.cols[player-1][row]==self.n: return player
        if row==col:
            self.diags[player-1]+=1
            if self.diags[player-1]==self.n: return player
        if row+col==self.n-1:
            self.adiags[player-1] += 1
            if self.adiags[player-1]==self.n: return player
        return 0         