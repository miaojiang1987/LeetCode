class Solution(object):
    def evaluate_expr(self,stack):
        result=stack.pop() if stack else 0
        
        while stack and stack[-1]!=')':
            sign=stack.pop()
            if sign=='+':
                result+=stack.pop()
            else:
                result-=stack.pop()
        return result
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        n,operand=0,0
        
        for i in range(len(s)-1,-1,-1):
            ch=s[i]
            if ch.isdigit():
                operand=(10**n*int(ch))+operand
                n+=1
            
            elif ch!=" ":
                if n:
                    stack.append(operand)
                    n,operand=0,0
                if ch=='(':
                    result=self.evaluate_expr(stack)
                    stack.pop()
                    stack.append(result)
                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        
        return self.evaluate_expr(stack)