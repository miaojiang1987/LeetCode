class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return 0
        m=len(num1)
        n=len(num2)
        
        if m>n:
            num2=(m-n)*'0'+num2
        if n>m:
            num1=(n-m)*'0'+num1
        
        flag=0
        result=''
        for i in range(max(m,n)-1,-1,-1):
            total= int(num1[i])+int(num2[i])+flag
            val=total%10
            result=str(val)+result
            flag=total//10
            
        if flag:
            result='1'+result
        
        
        return result