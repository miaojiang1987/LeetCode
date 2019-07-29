class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        P=[0]
        for x in A:
            P.append(P[-1]+x)
        N=len(A)
        dp=[0 for i in range(N)]
        for i in range(N):
            dp[i]=(P[N]-P[i])*1.0/(N-i)
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1,N):
                    dp[i]=max(dp[i],(P[j]-P[i])*1.0/ (j-i)+dp[j])
        return dp[0]