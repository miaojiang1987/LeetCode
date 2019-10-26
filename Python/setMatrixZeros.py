class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 0
        
        zero_set=set()
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]==0:
                    zero_set.add((x,y))
        
        for (x,y) in zero_set:
            for i in range(len(matrix[0])):
                matrix[x][i]=0
            for j in range(len(matrix)):
                matrix[j][y]=0
        
        
        return matrix