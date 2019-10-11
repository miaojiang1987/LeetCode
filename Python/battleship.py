class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        X, Y = len(board), len(board[0])
        
        def is_water(x, y):
            # check if the postion is in water
            if x<0 or y<0:
                return True
            elif x>=X or y >=Y:
                return True
            elif board[x][y] == '.':
                return True
            return False
        
        count = 0
        for i in range(X):
            for j in range(Y):
                # count first element of a shape: 2 sides are . or null
                if board[i][j] == 'X':
                    # Vertical Ship / Horizontal Ship: check left, up
                    if is_water(i, j-1) and is_water(i-1,j) :
                        count +=1
                          
        return count