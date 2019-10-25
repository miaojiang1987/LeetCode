class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2
        
        first,second=1,2
        result=0
        for i in range(2,n):
            result=first+second
            first=second
            second=result
        
        return result
        