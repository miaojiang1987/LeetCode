class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        if R == 0:
            return -1 
        C = len(grid[0])
        
        D = collections.defaultdict(int)
        D_numBuilding = collections.defaultdict(int)
        
        num_building = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1:
                    continue
                num_building += 1
                seen = set([(r,c)])
                my_queue = [((r,c),0)]
                while my_queue:
                    curr,level = my_queue.pop(0)
                    
                    if level > 0:
                        D[curr] += level
                        D_numBuilding[curr] += 1
                    
                    curr_x,curr_y = curr
                    nxt_points = {(curr_x+1,curr_y),(curr_x-1,curr_y),(curr_x,curr_y+1),(curr_x,curr_y-1)}
                    for nxt_x,nxt_y in nxt_points:
                        if 0 <= nxt_x < R and 0 <= nxt_y < C and grid[nxt_x][nxt_y] == 0:
                            if (nxt_x,nxt_y) not in seen:
                                seen.add((nxt_x,nxt_y))
                                my_queue.append(((nxt_x,nxt_y),level+1))
                                
        result = float('inf')
        for k in D_numBuilding:
            if D_numBuilding[k] == num_building:
                result = min(result,D[k])
        return result if result != float('inf') else -1