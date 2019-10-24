class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        digit=0
        n=x
        
        while n>0:
            n=n//10
            digit+=1
        
        
        result=0
        for i in range(digit//2):
            result=result*10+x%10
            x=x//10
        
        if digit%2!=0:
            x=x//10
        
        
        return result==x