class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board[0]) == 0:
            return False
        
        nrow = len(board)
        ncol = len(board[0])
        
        for i in range(nrow):
            for j in range(ncol):
                if self.dfs(board, i, j, word, 0):
                    return True
        
        return False
    
    def dfs(self, board, i, j, word, index):

        if index == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = ""  # suggest this cell has been used
        
        if self.dfs(board, i-1, j, word, index+1):
            return True
        if self.dfs(board, i+1, j, word, index+1):
            return True
        if self.dfs(board, i, j-1, word, index+1):
            return True
        if self.dfs(board, i, j+1, word, index+1):
            return True
        
        board[i][j] = temp
        
        return False