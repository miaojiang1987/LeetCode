class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result=[]
        if not nums:
            return result
        nums.sort()
        temp=[]
        visited=[0 for i in range(len(nums))]
        
        self.dfs(result,temp,visited,nums)
        return result
    
    def dfs(self,result,temp,visited,nums):
        if len(temp)==len(nums):
            result.append(temp+[])
            return
        
        for i in range(len(nums)):
            if visited[i]: continue
            if i>0 and nums[i]==nums[i-1] and not visited[i-1]: continue
            temp.append(nums[i])
            visited[i]=1
            self.dfs(result,temp,visited,nums)
            temp.pop()
            visited[i]=0