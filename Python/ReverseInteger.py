class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if x<0 else 1
        val=abs(x)
        answer=0
        while val>0:
            answer=answer*10+val%10
            val=val//10
     
        if answer > pow(2, 31)-1:
            return 0
        return sign*answer