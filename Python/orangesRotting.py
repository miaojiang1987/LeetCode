class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        queue=[]
        fresh=0
        time=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        if fresh==0:
            return 0
        
        while queue:
            size=len(queue)
            for k in range(size):
                x,y=queue.pop(0)
                
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    X=x+dx
                    Y=y+dy
                    if X<0 or Y<0 or X>=row or Y>=col or grid[X][Y]!=1:
                        continue
                    grid[X][Y]=2
                    queue.append((X,Y))
                    fresh-=1
            time+=1
        
        if fresh!=0:
            return -1
        
        return time-1