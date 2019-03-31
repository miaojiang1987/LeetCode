class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid)==0:
            return 0
        row=len(grid)
        col=len(grid[0])
        visited=set()
        
        queue=[]
        max_area=0
        
        for i in range(row):
            for j in range(col):
                if (i,j) in visited: continue
                if grid[i][j]==1:
                    queue.append((i,j))
                    count=1
                    visited.add((i,j))
                    while queue:
                        x,y=queue.pop(0)
                    
                        for (dx,dy) in [(0,1),(1,0),(0,-1),(-1,0)]:
                            X=x+dx
                            Y=y+dy
                            if X>=0 and Y>=0 and X<row and Y<col and (X,Y) not in visited and grid[X][Y]==1:
                                count+=1
                                visited.add((X,Y))
                                queue.append((X,Y))
                    max_area=max(max_area,count)
            
        return max_area