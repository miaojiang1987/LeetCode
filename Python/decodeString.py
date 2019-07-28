class Solution(object):
    def decodeString(self, s):
        if not s:
            return ''
        
        res = []
        stack = []
        
        for i, x in enumerate(s,0):
            if x.isdigit():
                if i > 0 and s[i-1].isdigit():
                    stack[-1][0] = stack[-1][0] * 10 + int(x)
                else:
                    stack.append([int(x),'']) 
					
            elif x.isalpha():
                if not stack:
                    res += x
                else:
                    stack[-1][1] += x
					
            elif x == ']':
			
                n, chars = stack.pop()
				
		""" non-empty stack means nested []'s, so append the string to the inner []'s string"""
                if stack:
                    stack[-1][1] += chars * n
                else:
                    res += chars * n  
            
        return ''.join(res)