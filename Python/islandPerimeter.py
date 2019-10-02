class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        result=0
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n]==1:
                    for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
                        dx,dy=direction
                        X=m+dx
                        Y=n+dy
                        if X<0 or Y<0 or X>=len(grid) or Y>=len(grid[0]):
                            result+=1
                        elif grid[X][Y]==0:
                            result+=1
        
        
        return result
                    