class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        result=0
        row=len(grid)
        col=len(grid[0])
        visited=set()
        queue=collections.deque()
        
        for i in range(row):
            for j in range(col):
                if (i,j) in visited: continue
                
                if grid[i][j]=='1':
                    result+=1
                    queue.append((i,j))
                    visited.add((i,j))
                    
                    while queue:
                        x,y=queue.popleft()
                        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                            X=x+dx
                            Y=y+dy
                            if X>=0 and Y>=0 and X<row and Y<col and (X,Y) not in visited and grid[X][Y]=='1':
                                queue.append((X,Y))
                                visited.add((X,Y))
        
        
        return result