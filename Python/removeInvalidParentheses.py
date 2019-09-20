class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l=0
        r=0
        result=[]
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            if s[i]==')':
                if l>0:
                    l-=1
                else:
                    r+=1
        
        self.dfs(result,s,l,r,0)
        return result
    
    def isValid(self,s):
        counter=0
        for c in s:
            if counter<0:
                return False            
            if c=='(':
                counter+=1
            
            if c==')':
                counter-=1
        
        return counter==0
    
    def dfs(self,result,s,l,r,start):
        if l==0 and r==0 and self.isValid(s):
            result.append(s)
            return
        
        for i in range(start,len(s)):
            if i!=start and s[i]==s[i-1]:
                continue
            
            if s[i]=='(' and l>0:
                 self.dfs(result,s[:i]+s[i+1:],l-1,r,i)
            
            if s[i]==')' and r>0:
                self.dfs(result,s[:i]+s[i+1:],l,r-1,i)