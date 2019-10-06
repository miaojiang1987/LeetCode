class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return None
        
        check=set()
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    check.add((i,j))
        
        for x,y in check:
            for i in range(n):
                matrix[x][i]=0
            for j in range(m):
                matrix[j][y]=0
        
        
        return matrix