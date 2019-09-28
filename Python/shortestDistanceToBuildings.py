class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R=len(grid)
        C=len(grid[0])
        if not R or not C:
            return 0
        visited=set()
        D=collections.defaultdict(int)
        D_buildings=collections.defaultdict(int)
        
        number_of_buildings=0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]!=1:
                    continue
                number_of_buildings+=1
                visited=set((i,j))
                queue=[((i,j),0)]
                
                while queue:
                    cur,level=queue.pop(0)
                    
                    if level>0:
                        D[cur]+=level
                        D_buildings[cur] += 1
                    
                    cur_X,cur_Y=cur
                    
                    next_points={(cur_X+1,cur_Y),(cur_X,cur_Y+1),(cur_X-1,cur_Y),(cur_X,cur_Y-1)}
                    
                    for next_point_x,next_point_y in next_points:
                        if 0<=next_point_x<R and 0<=next_point_y<C and grid[next_point_x][next_point_y] == 0:
                            if (next_point_x,next_point_y) not in visited:
                                visited.add((next_point_x,next_point_y))
                                queue.append(((next_point_x,next_point_y),level+1))
        
        res = float('inf')
        for k in D_buildings:
            if D_buildings[k] == number_of_buildings:
                res = min(res,D[k])
        return res if res != float('inf') else -1