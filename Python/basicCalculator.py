class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        num=0 
        pre_op='+'
        
        for i in range(len(s)):
            if s[i] in '0123456789':
                num=num*10+int(s[i])
            
            if i==len(s)-1 or s[i] in '+-*/':
                if pre_op=='+':
                    stack.append(num)
                elif pre_op=='-':
                    stack.append(-num)
                elif pre_op=='*':
                    pre_num=stack.pop()
                    num=num*pre_num
                    stack.append(num)
                elif pre_op=='/':
                    pre_num=stack.pop()
                    if num*pre_num < 0:
                        result=abs(pre_num)//num
                        stack.append(-1*result)
                    else:
                        stack.append(pre_num//num)
                
                pre_op=s[i]
                num=0
        
        
        
        return sum(stack)