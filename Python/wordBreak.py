class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDictSet=set()
        queue=[]
        visited=set()
        queue.append(0)
        
        while queue:
            start=queue.pop()
            if start not in visited:
                for i in range(start+1,len(s)+1):
                    if s[start:i] in wordDict:
                        queue.append(i)
                        if (i==len(s)):
                            return True
                
                visited.add(start)
        
        return False