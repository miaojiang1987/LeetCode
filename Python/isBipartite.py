class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited=[0]*len(graph)
        queue = collections.deque()
        for i in range(len(graph)):
            if graph[i] and visited[i]==0:
                queue.append(i)
                visited[i]=1
            
                while queue:
                    node=queue.popleft()
                    for nei in graph[node]:
                        if visited[nei]==0:
                            visited[nei]=3-visited[node]
                            queue.append(nei)
                        
                        if visited[nei]==visited[node]:
                            return False
        
        
        return True