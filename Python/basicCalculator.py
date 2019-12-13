class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign=1
        result=0
        
        i=0
        stack=[]
        while i<len(s):
            if s[i] in "0123456789":
                num=0
                while i<len(s) and s[i] in "0123456789":
                    num=10*num+int(s[i])
                    i+=1
                result+=sign*num
                i-=1
            
            elif s[i]=='+':
                sign=1
            
            elif s[i]=='-':
                sign=-1
            
            elif s[i]=='(':
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            
            elif s[i]==')':
                result *= stack.pop()
                result += stack.pop()
            
            i+=1
            
        return result