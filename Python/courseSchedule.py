class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph={}
        indegree={}
        
        for i in range(numCourses):
            indegree[i]=0
            graph[i]=[]
        
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        
        count=0
        queue=collections.deque()
        
        for course in indegree:
            if indegree[course]==0:
                queue.append(course)
        
        while queue:
            node=queue.popleft()
            count+=1
            
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        
        return count==numCourses