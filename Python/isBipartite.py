class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [0]*len(graph)
        queue=collections.deque()
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                queue.append(i)
                visited[i]=1
                
                while queue:
                    v=queue.popleft()
                    for node in graph[v]:
                        if visited[node]==0:
                            queue.append(node)
                            visited[node]=3-visited[v]
                        if visited[node]==visited[v]:
                            return False
            
        
        return True