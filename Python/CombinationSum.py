class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result=[]
        if not candidates or len(candidates)==0: return result
        
        temp=[]
        self.dfs(candidates,target,temp,result,0)
        return result
    
    
    def dfs(self,candidates,target,temp,result,start):
        if target==0:
            result.append(temp+[])
            return
        
        if target<0:
            return
        
        for i in range(start,len(candidates)):
            temp.append(candidates[i])
            self.dfs(candidates,target-candidates[i],temp,result,i)
            temp.pop()
