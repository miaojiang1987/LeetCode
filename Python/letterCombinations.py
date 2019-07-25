class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.keyboard={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv',
                       '9':'wxyz'}
        
        if not digits or len(digits)==0:
            return []
        
        result=[]
        temp=''
        self.dfs(digits,temp,result,0)
        return result
    
    def dfs(self,digits,temp,results,num):
        if len(temp)==len(digits):
            results.append(temp)
            return
        
        for char in self.keyboard[digits[num]]:
            temp+=char
            self.dfs(digits,temp,results,num+1)
            temp=temp[:-1]