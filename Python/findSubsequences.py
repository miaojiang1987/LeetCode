class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res=[]
        
        def dfs(index,nums, cur, res):
            if index==len(nums)+1:
                return
            if len(cur)>1: res.append(tuple(cur))
            for i in range(index, len(nums)):
                if not cur or (cur and cur[-1]<=nums[i]):
                    dfs(i+1, nums, cur+[nums[i]], res)

        dfs(0,nums, [], res)
        res= list(set(res))
        return [list(item) for item in res]