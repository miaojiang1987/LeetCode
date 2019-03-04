class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs)==0:
            return 0
        
        dp=[[0 for i in range(3)] for j in range(len(costs))]
        for i in range(3):
            dp[0][i]=costs[0][i]
        
        for i in range(1,len(costs)):
            dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i][1]
            dp[i][2]=min(dp[i-1][0],dp[i-1][1])+costs[i][2]
        
        n=len(costs)-1
        return min(dp[n][0],dp[n][1],dp[n][2])