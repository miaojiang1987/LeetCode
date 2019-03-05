class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        
        if n<0:
            return 1.0/self.helper(x,abs(n))
        
        else:
            return self.helper(x,n)
        
        
    def helper(self,x,n):
        if n==0:
            return 1
        half=self.helper(x,n/2)
        if n%2==0:
            return half*half
        
        else:
            return half*half*x
        