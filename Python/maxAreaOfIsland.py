class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid)==0:
            return 0
        row=len(grid)
        columns=len(grid[0])
        visited=set()
        queue=[]
        
        max_area=0
        #queue.append((0,0))
        
        for i in range(row):
            for j in range(columns):
                if (i,j) in visited: continue
                if grid[i][j]==1:
                    queue.append((i,j))
                    current_area=1
                    visited.add((i,j))
                    while queue:
                        x,y=queue.pop(0)
                        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                            X=x+dx
                            Y=y+dy
                            if X>=0 and Y>=0 and Y<columns and X<row and grid[X][Y]==1 and (X,Y) not in visited:
                                visited.add((X,Y))
                                queue.append((X,Y))
                                current_area+=1
                    max_area=max(current_area,max_area)
        return max_area