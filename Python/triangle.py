class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        dp=[0]*len(triangle)
        
        for row in triangle:
            oldDp=dp[:]
            for i in range(len(row)):
                if i==0:
                    dp[i]=oldDp[i]+row[i]
                
                elif i==len(row)-1:
                    dp[i]=oldDp[i-1]+row[i]
                
                else:
                    dp[i]=min(oldDp[i-1],oldDp[i])+row[i]
            #print(dp)
        
        return min(dp)