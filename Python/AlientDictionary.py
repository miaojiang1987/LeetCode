class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph={}
        indegree={}
        
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c]=[]
                    indegree[c]=0
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].append(word2[j])
                        indegree[word2[j]]+=1
                    break
        
        result=""
        queue=collections.deque()
        
        for item in indegree:
            if indegree[item]==0:
                queue.append(item)
        
        while queue:
            cur=queue.popleft()
            result+=cur
            for nei in graph[cur]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        if len(result) == len(indegree):
            return result
        return ""