class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m=len(num1)
        n=len(num2)
        
        array=[0 for i in range(m+n-1)]
        
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                array[i+j]+=int(num1[i])*int(num2[j])
        
        result=""
        
        carry=0
        
        for k in range(len(array)-1,-1,-1):
            result=str((array[k]+carry)%10)+result
            carry= (array[k]+carry)//10
        
        if carry>0:
            result=(str)(carry)+result
        
        if len(result) > 1 and result[0] == "0":
            return "0"
        
        return result