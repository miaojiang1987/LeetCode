class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 1. use DFS to find one island and put the id of all cells associated with
        # this island to a list, island
        self.nbs = [[-1,0], [1, 0], [0, -1], [0, 1]]
        visited = [[0]*len(A[0]) for _ in range(len(A))]
        island = []
        for idx in range(len(A)):
            for idy in range(len(A[0])):
                if A[idx][idy] == 1:
                    self.dfs(A, visited, idx, idy, island)
                    break
            else:
                continue
            break
            
        # 2. use BFS to expand this island
        while island:
            pos, step = island.pop(0)
            for nb in self.nbs:
                i = pos[0] + nb[0]
                j = pos[1] + nb[1]
                if i >=0 and i<len(A) and j>=0 and j<len(A[0]) and not visited[i][j]:
                    if A[i][j] == 1:
                        return step
                    island.append(([i,j], step+1))
                    visited[i][j] = 1
        
        
        
    def dfs(self, A, visited, idx, idy, island):
        if idx<0 or idx>=len(A) or idy<0 or idy>=len(A[0]) or visited[idx][idy] or A[idx][idy]==0:
            return
        visited[idx][idy] = 1
        island.append(([idx, idy], 0))
        for nb in self.nbs:
            self.dfs(A, visited, idx+nb[0], idy+nb[1], island)