class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative=False
        if n<0:
            negative=True
            n=abs(n)
        if n==0:
            return 1
        if x==0:
            return 0
        
        ans=1.0
        cur_ans=x
        
        while n>0:
            if n%2==1:
                ans=ans* cur_ans
            
            cur_ans*=cur_ans
            n=n//2
        
        if negative:
            return 1.0/ans
        else:
            return ans