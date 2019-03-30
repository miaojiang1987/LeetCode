class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        
        count=0
        graph=collections.defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        queue=[]
        visited=set()
        
        for i in range(n):
            if i in visited: continue
            queue.append(i)
            visited.add(i)
            count+=1
            
            while queue:
                node=queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        return count