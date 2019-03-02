class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        column=len(obstacleGrid[0])
        row=len(obstacleGrid)
        
        result=[[0 for i in range(column)] for j in range(row)]
        for i in range(column):
            if obstacleGrid[0][i]==1:
                result[0][i]=0
                break
            else:
                result[0][i]=1
                
        for j in range(row):
            if obstacleGrid[j][0]==1:
                result[j][0]=0
                break
            else:
                result[j][0]=1
        
        for i in range(1,row):
            for j in range(1,column):
                if obstacleGrid[i][j]==1:
                    result[i][j]=0
                else:
                    result[i][j]=result[i-1][j]+result[i][j-1]
        
        
        return result[row-1][column-1]