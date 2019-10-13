class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return None
        
        graph={}
        indegree={}
        
        for word in words:
            for c in word:
                graph[c]=[]
                indegree[c]=0
        
        for i in range(1,len(words)):
            word1=words[i-1]
            word2=words[i]
            
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        indegree[word2[j]]+=1
                        graph[word1[j]].append(word2[j])
                    break
       
        result=""
        queue=collections.deque()
        for key in indegree:
            if indegree[key]==0:
                queue.append(key)
        
        while queue:
            node=queue.popleft()
            
            result+=node
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
            
        
        if len(result)!=len(indegree):
            return ""
        
        return result