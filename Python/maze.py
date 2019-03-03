class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        
        dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
        
        visited = set()
        
        q = collections.deque([tuple(start)])
        
        while q:
            pos = q.popleft()
            if pos in visited: continue
            visited.add(pos)
            if pos == tuple(destination): return True
            for i in xrange(4):
                x, y = pos[0] + dx[i], pos[1] + dy[i]
                
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
                    x += dx[i]
                    y += dy[i]
                x -= dx[i]
                y -= dy[i]
                if maze[x][y] != 1:
                    q.append((x, y))
        return False