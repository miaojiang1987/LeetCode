class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if divisor==1:
            return dividend
        negative=(dividend<0)^(divisor<0)
        dvd = abs(dividend)
        dvs = abs(divisor)
        res=0
        
        while dvd>=dvs:
            temp=dvs
            m=1
            
            while temp<<1<dvd:
                temp<<=1
                m<<=1
            
            dvd-=temp
            res+=m
        
        if not negative:
            return res
        else:
            return ~res+1