class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0

        
        left=0
        right=x
     
        
        while left<=right:
            mid=(right+left)//2
            if mid*mid==x:
                return mid
            
            if mid*mid>x:
                right=mid-1
            
            else:
                left=mid+1
        
        
        return right