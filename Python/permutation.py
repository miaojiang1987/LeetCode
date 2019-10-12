class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        
        result=[]
        temp=[]
        visited=set()
        self.dfs(result,temp,visited,nums)
        
        return result
    
    def dfs(self,result,temp,visited,nums):
        if len(temp)==len(nums):
            result.append(temp+[])
            return
        
        
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            temp.append(nums[i])
            visited.add(nums[i])
            self.dfs(result,temp,visited,nums)
            temp.pop()
            visited.remove(nums[i])