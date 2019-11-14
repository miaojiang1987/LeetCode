class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack=[]
        hashmap={')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in hashmap:
                top=stack.pop() if stack else '#'
                if hashmap[s[i]]!=top:
                    return False
            else:
                stack.append(s[i])
        
        
        return not stack