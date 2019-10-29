class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m=len(a)
        n=len(b)
        
        if m>n:
            b='0'*(m-n)+b
        if n>m:
            a='0'*(n-m)+a

        result=''
        carry=0
        for i in range(max(m,n)-1,-1,-1):
            print(a)
            val=carry+int(a[i])+int(b[i])
            carry=val//2
            val=val%2
        
            
            result=str(val)+result
            
        if carry:
            result='1'+result
        
        
        return result