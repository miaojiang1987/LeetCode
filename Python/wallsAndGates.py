class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 0
        
        m=len(rooms)
        n=len(rooms[0])
        
        queue=collections.deque()
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i,j,0))
        
        while queue:
            x,y,val=queue.popleft()
            for dx,dy in direction:
                newX=x+dx
                newY=y+dy
                
                if 0<=newX<m and 0<=newY<n and rooms[newX][newY] == 2**31-1:
                    rooms[newX][newY]=val+1
                    queue.append((newX,newY,val+1))
            
        
        return