class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1)!=len(words2): return False
     
        
        graph=collections.defaultdict(list)
        for w1,w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)
        
        for w1,w2 in zip(words1,words2):
            stack=[w1]
            seen={w1}
            while stack:
                word=stack.pop()
                if word==w2: break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True