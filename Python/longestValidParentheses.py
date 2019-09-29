class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen=0
        stack=[]
        stack.append(-1)
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                
                else:
                    maxLen=max(maxLen,i-stack[-1])
                    
        
        return maxLen