class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-1 for i in range(amount+1)]
        
        dp[0]=0
        
        for j in range(1,len(dp)):
            for coin in coins:
                if j-coin>=0 and dp[j-coin]!=-1:
                    if dp[j]==-1:
                        dp[j]=dp[j-coin]+1
                    else:
                        dp[j]=min(dp[j-coin]+1,dp[j])
        
        
        return dp[amount]