class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins: return -1
         
        dp=[-1 for i in range(amount+1)]
        dp[0]=0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    if dp[i]==-1:
                        dp[i]=dp[i-coin]+1
                    else:
                        dp[i]=min(dp[i-coin]+1,dp[i])
        
        
        return dp[amount]