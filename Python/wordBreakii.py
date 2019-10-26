class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        tokenDict={}
        return self.dfs(s,tokenDict,wordDict)
    
    def dfs(self,s,tokenDict,wordDict):
        result=[]
        if s in wordDict:
            result.append(s)
        for i in range(len(s)-1):
            prefix,suffix=s[:i+1],s[i+1:]
            if prefix not in wordDict:
                continue
            rest=[]
            if suffix in tokenDict:
                rest=tokenDict[suffix]
            else:
                rest=self.dfs(suffix,tokenDict,wordDict)
            
            for n in rest:
                result.append(prefix + ' ' + n)
        
        tokenDict[s]=result
        return result