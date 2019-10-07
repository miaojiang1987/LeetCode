class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result=[]
        temp=[]

        self.dfs(nums,result,temp,0)
        return result
    
    def dfs(self,nums,result,temp,start):
        result.append(temp+[])
        if len(temp)==len(nums):
            return
        
        for i in range(start,len(nums)):
            temp.append(nums[i])
            #result.append(temp+[])
            self.dfs(nums,result,temp,i+1)
            temp.pop()
        