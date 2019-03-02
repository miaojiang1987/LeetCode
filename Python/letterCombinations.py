class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.keyboard={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        if not digits or len(digits)==0:
            return []
        
        result=[]
        
        self.dfs(digits,'',result,0)
        return result
    
    def dfs(self,digits,temp,result,pos):
        
        if len(temp)==len(digits):
            result.append(temp)
            return 
        
        for char in self.keyboard[digits[pos]]:
            temp=temp+char
            self.dfs(digits,temp,result,pos+1)
            temp=temp[:-1]