class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # initialize graph and indegree
        graph = {}
        indegree = {}
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []
        
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
            
        count = 0
        queue = collections.deque()
        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses