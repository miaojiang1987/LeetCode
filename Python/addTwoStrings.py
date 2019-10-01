class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return 0
        if not num1:
            return int(num2)
        if not num2:
            return int(num1)
        
        m=len(num1)
        n=len(num2)
        
        if m > n:
            num2 = "0" * (m-n) + num2
        else:
            num1 = "0" * (n-m) + num1
        
        maxLen=max(m,n)
        result=''
        
        carry=0
        for i in range(maxLen-1,-1,-1):
            a=int(num1[i])
            b=int(num2[i])
            result=str((a+b+carry)%10)+result
            carry=(a+b+carry)//10
        
        
        if carry:
            result='1'+result
        
        return result