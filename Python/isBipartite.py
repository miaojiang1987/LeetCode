class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        visited=[0]*len(graph)
        
        for i in range(len(graph)):
            if visited[i] or len(graph[i])==0:
                continue
            
            queue=collections.deque()
            queue.append(i)
            
            while queue:
                node=queue.popleft()
                
                for nei in graph[node]:
                    if visited[nei]==0:
                        queue.append(nei)
                        visited[nei]=3-visited[node]
                    
                    if visited[nei]==visited[node]:
                        return False
            
            
        
        return True