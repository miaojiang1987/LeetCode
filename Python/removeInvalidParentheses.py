class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        result=[]
        left=0
        right=0
        
        for i in range(len(s)):
            if s[i]=='(':
                left+=1
            elif s[i]==")":
                if left>0:
                    left-=1
                else:
                    right+=1
        
        
        self.dfs(result,s,0,left,right)
        return result
    
    def isValid(self,s):
        count=0
        for c in s:
            if count<0:
                return False
            if c=='(':
                count+=1
            elif c==')':
                count-=1
        
        return count==0
    
    def dfs(self,result,s,start,l,r):
        if l==0 and r==0 and self.isValid(s):
            result.append(s)
            return
        
        for i in range(start,len(s)):
            if s[i]=='(' and l>0 and (i==start or s[i] != s[i-1]):
                self.dfs(result,s[:i]+s[i+1:],i,l-1,r)
            
            if s[i]==')' and r>0 and (i==start or s[i]!=s[i-1]):
                self.dfs(result,s[:i]+s[i+1:],i,l,r-1)