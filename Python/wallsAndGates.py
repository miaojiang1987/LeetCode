class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return None
        
        row=len(rooms)
        col=len(rooms[0])
        
        queue=collections.deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j]==0:
                    queue.append(((i,j),0))
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        while queue:
            position,value=queue.popleft()
            x,y=position[0],position[1]
            
            for dx,dy in directions:
                X=x+dx
                Y=y+dy
                
                if 0<=X<row and 0<=Y<col and rooms[X][Y] == 2**31-1:
                    rooms[X][Y]=value+1
                    queue.append(((X,Y),value+1))
            
        
        return