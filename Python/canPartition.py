class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        total=sum(nums)
        if total%2:
            return False
        
        target=total//2
        
        dp=[False]*(target+1)
        dp[0]=True
        
        for num in nums:
            if num==target:
                return True
            if num>target:
                return False
            for i in range(target,num-1,-1):
                dp[i]=dp[i-num] or dp[i]
        
        
        return dp[target]