class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        res=[]
        stack=[]
        
        for i, x in enumerate(s,0):
            if x.isdigit():
                if i>0 and s[i-1].isdigit():
                    stack[-1][0]=stack[-1][0] * 10 + int(x)
                else:
                    stack.append([int(x),''])
            
            elif x.isalpha():
                if not stack:
                    res += x
                else:
                    stack[-1][1] += x
            
            elif x==']':
                n,chars=stack.pop()
                if stack:
                    stack[-1][1]+=n*chars
                else:
                    res+=n*chars
            
        
        
        return ''.join(res)