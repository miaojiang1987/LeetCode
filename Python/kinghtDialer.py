class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp=[1]*10
        
        for hops in range(N-1):
            dp1=[0]*10
            for node,count in enumerate(dp):
                for nei in moves[node]:
                    dp1[node]+=dp[nei]
                    dp1[node]%=MOD
            
            dp=dp1
        
        return sum(dp)%MOD