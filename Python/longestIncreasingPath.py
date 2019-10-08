class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        result=0
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0 for i in range(col)] for j in range(row)]
        
        for i in range(row):
            for j in range(col):
                max_path=self.dfs(matrix,i,j,dp)
                result=max(result,max_path)
        
        
        return result
    
    
    def dfs(self,matrix,i,j,dp):
        if dp[i][j]!=0:
            return dp[i][j]
        max_path=1
        
        m = len(matrix)
        n = len(matrix[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        for dx,dy in directions:
            X=i+dx
            Y=j+dy
            
            if X>=0 and X<m and Y>=0 and Y<n and matrix[i][j]<matrix[X][Y]:
                num_path=self.dfs(matrix,X,Y,dp)+1
                max_path=max(max_path,num_path)
        
        dp[i][j] = max_path