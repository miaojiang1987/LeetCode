class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if not candidates or len(candidates)==0:
            return result
        candidates.sort()
        temp=[]
        self.dfs(candidates,target,result,temp,0)
        return result
    
    def dfs(self,candidates,target,result,temp,start):
        
        if target==0:
            result.append(temp+[])
            return
        
        if target<0:
            return
        
        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            temp.append(candidates[i])
            self.dfs(candidates,target-candidates[i],result,temp,i+1)
            temp.pop()