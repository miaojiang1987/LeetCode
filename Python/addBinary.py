class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)<len(b):
            a,b=b,a
        
        b='0'*(len(a)-len(b))+b
        result=''
        flag=0
        for i in range(len(a)-1,-1,-1):
            _sum=int(a[i])+int(b[i])+flag
            flag=_sum//2
            _sum=_sum%2
            result=(str)(_sum)+result
        
        if flag==1:
            result='1'+result
        
        
        return result