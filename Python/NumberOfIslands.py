class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        
        number=0
        visited=set()
        queue=[]
        
        for i in range(row):
            for j in range(col):
                if (i,j) in visited: continue
                if grid[i][j]=='1':
                    number+=1
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        x,y=queue.pop(0)
                        for (dx,dy) in [(0,1),(1,0),(-1,0),(0,-1)]:
                            X=x+dx
                            Y=y+dy
                            if X>=0 and X<row and Y>=0 and Y<col and grid[X][Y]=='1' and (X,Y) not in visited:
                                queue.append((X,Y))
                                visited.add((X,Y))
        
        return number