class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        _len=len(nums)
        dp=[collections.defaultdict(int) for i in range(_len+1)]
        dp[0][0]=1
        for i in range(len(nums)):
            num=nums[i]
            for sum,cnt in dp[i].items():
                dp[i+1][sum+num]+=cnt
                dp[i+1][sum-num]+=cnt
        
        
        return dp[_len][S]