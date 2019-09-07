class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph,indegree=self.buildgraph(words)
        result=""
        queue=collections.deque()
        for char in indegree:
            if indegree[char]==0:
                queue.append(char)
        
        while queue:
            cur=queue.popleft()
            result+=cur
            for char in graph[cur]:
                indegree[char]-=1
                if indegree[char]==0:
                    queue.append(char)
        
        if len(result)!=len(indegree): 
            return ""
        return result
    
    def buildgraph(self,words):
        graph={}
        indegree={}
        
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c]=set()
                indegree[c]=0
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            if word1!=word2:
                length=min(len(word1),len(word2))
                for j in range(length):
                    c1=word1[j]
                    c2=word2[j]
                    if c1!=c2:
                        if c2 not in graph[c1]:
                            graph[c1].add(c2)
                            indegree[c2]+=1
                        break
        
        return graph,indegree