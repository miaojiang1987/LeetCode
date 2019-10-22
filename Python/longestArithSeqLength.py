class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        if len(A)<=2:
            return len(A)
        dp=[{} for i in range(len(A))]
        result=0
        
        for i in range(len(A)):
            for j in range(i):
                diff=A[i]-A[j]
                if diff in dp[j]:
                    dp[i][diff]=dp[j][diff]+1
                
                else:
                    dp[i][diff]=2
                
                result=max(result,dp[i][diff])
        
        
        return result