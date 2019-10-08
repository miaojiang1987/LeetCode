class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        row=len(board)
        col=len(board[0])
        
        visited=[[0 for j in range(col)] for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                if self.dfs(board,word,0,visited,i,j):
                    return True
        
        
        return False
    
    
    def dfs(self,board,word,start,visited,i,j):
        
        if start==len(word):
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited[i][j]==1 or board[i][j]!=word[start]:
            return False
        
        visited[i][j]=1
        
        if self.dfs(board,word,start+1,visited,i+1,j):
            return True
        
        if self.dfs(board,word,start+1,visited,i-1,j):
            return True
        
        if self.dfs(board,word,start+1,visited,i,j+1):
            return True
        
        if self.dfs(board,word,start+1,visited,i,j-1):
            return True
        
        visited[i][j]=0
        return False