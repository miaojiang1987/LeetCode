from collections import deque

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        start_r, start_c = start
        end_r, end_c = destination
        queue = deque([(start_r, start_c, i) for i in xrange(4)])
        dist = {(start_r, start_c, i): 0 for i in xrange(4)}
        while queue:
            r, c, d = queue.popleft()
            if self.can_move(maze, r, c, d):
                new_r, new_c = self.get_new_position(r, c, d)
                if (new_r, new_c, d) not in dist:
                    dist[(new_r, new_c, d)] = dist[(r, c, d)]+1
                    queue.append((new_r, new_c, d))
            else:
                if r == end_r and c == end_c:
                    return dist[(r, c, d)]
                for i in xrange(4):
                    if (r, c, i) not in dist:
                        dist[(r, c, i)] = dist[(r, c, d)]
                        queue.appendleft((r, c, i))
        return -1
    
    def can_move(self, maze, r, c, d):
        new_r, new_c = self.get_new_position(r, c, d)
        if new_r < 0 or new_c < 0 or new_r >= len(maze) or new_c >= len(maze[0]) or maze[new_r][new_c] == 1:
            return False
        return True
    
    def get_new_position(self, r, c, d):
        if d == UP:
            return r-1, c
        elif d == DOWN:
            return r+1, c
        elif d == LEFT:
            return r, c-1
        else:
            return r, c+1