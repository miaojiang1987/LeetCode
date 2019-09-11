class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        dp = [0] * len(height)
        
        maxLen = 0
        for i in range(len(height)):
            dp[i] = maxLen
            maxLen = max(maxLen, height[i])
            
        maxLen = 0
        for i in range(len(height)-1, -1, -1):
            dp[i] = min(maxLen, dp[i])
            maxLen = max(maxLen, height[i])
            if dp[i] > height[i]:
                res += dp[i] - height[i]
                
        return res