class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        first,second='XO'
        x_count=sum(row.count(first) for row in board)
        o_count=sum(row.count(second) for row in board)
        
        if o_count not in {x_count-1, x_count}: return False
        if self.win(board, first) and x_count-1 != o_count: return False
        if self.win(board, second) and x_count != o_count: return False

        return True

    def win(self,board,player):
        for i in xrange(3):
            if all(board[i][j] == player for j in xrange(3)):
                return True
            if all(board[j][i] == player for j in xrange(3)):
                return True

        return (player == board[1][1] == board[0][0] == board[2][2] or player == board[1][1] == board[0][2] == board[2][0])