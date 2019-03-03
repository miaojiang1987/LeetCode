class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums)==0:
            return []
        
        result=[]
        temp=[]
        self.dfs(nums,result,temp,0)
        return result
    
    def dfs(self,nums,result,temp,start):
        result.append(temp+[])
        
        for i in range(start,len(nums)):
            self.dfs(nums,result,temp+[nums[i]],i+1)