class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) == 0:
            return 0        
        
        m = len(matrix)
        n = len(matrix[0])
        res = 1
        
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(dp, matrix, i, j))
        
        return res
    
    
    def dfs(self, dp, matrix, i, j):
        
        #dp在这里的作用是，如果之前已经算过了，只需查表，无需重复计算了
        if dp[i][j] != 0:
            return dp[i][j]
        
        maxLen = 1
        m = len(matrix)
        n = len(matrix[0])
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = i+dx
            y = j+dy
            if x >= 0 and x < m and y >= 0 and y < n and matrix[i][j] < matrix[x][y]:
                length = self.dfs(dp, matrix, x, y) + 1
                maxLen = max(maxLen, length)
        
        dp[i][j] = maxLen
        return maxLen