class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        visited=set()
        queue=[]
        result=0
        
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if (i,j) in visited: continue
                if grid[i][j]=='1':
                    queue.append((i,j))
                    visited.add((i,j))
                    result+=1
                    while queue:
                        x,y=queue.pop(0)
                        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                            X=x+dx
                            Y=y+dy
                            if X>=0 and Y>=0 and X<row and Y<col and (X,Y) not in visited and grid[X][Y]=='1':
                                queue.append((X,Y))
                                visited.add((X,Y))
        
        return result