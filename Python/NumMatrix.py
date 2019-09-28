class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.dp=[]
            return
        
        row,col=len(matrix),len(matrix[0])
        
        self.dp=[[0 for i in range(col+1)] for j in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.dp[i][j]=matrix[i-1][j-1]+self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]
        
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.dp:
            return 0
        
        return self.dp[row2+1][col2+1]+self.dp[row1][col1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]