class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if not candidates:
            return []
        temp=[]
        self.dfs(candidates,target,0,result,temp)
        return result
    
    def dfs(self,candidates,target,start,result,temp):
        if target==0:
            result.append(temp+[])
            
        if target<0:
            return
        
        for i in range(start,len(candidates)):
            number=candidates[i]
            temp.append(number)
            self.dfs(candidates,target-number,i,result,temp)
            temp.pop()