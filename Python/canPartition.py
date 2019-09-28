class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        if not nums:
            return False
        
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum // 2
        
        dp = [False]*(target + 1) #初始化dp，全部设为false
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1): #要更新[nums[i], target]之间的值
                print(dp)
                print(j)
                if dp[j-nums[i]] == True:  
                    dp[j] = True
                #dp[j] = dp[j-nums[i]] or dp[j]
        return dp[target]