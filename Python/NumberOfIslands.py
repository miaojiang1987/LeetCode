class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m=len(grid)
        n=len(grid[0])
        
        visited=set()
        queue=collections.deque()
        result=0
        
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                
                if grid[i][j]=='1':
                    result+=1
                    queue.append((i,j))
                    visited.add((i,j))
                    
                    while queue:
                        x,y=queue.popleft()
                        
                        for (dx,dy) in [(0,1),(1,0),(0,-1),(-1,0)]:
                            X=x+dx
                            Y=y+dy
                            
                            if X>=0 and X<m and Y>=0 and Y<n and grid[X][Y]=='1' and (X,Y) not in visited:
                                queue.append((X,Y))
                                visited.add((X,Y))
        
        return result