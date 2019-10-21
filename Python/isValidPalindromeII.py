class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left=0
        right=len(s)-1
        if self.isValid(s,left,right):
            return True
        while left<=right:
            if s[left]!=s[right]:
                return self.isValid(s,left+1,right) or self.isValid(s, left, right-1)
            left+=1
            right-=1
        
        return False
        
        
    
    def isValid(self,s,l,r):
        left=l
        right=r
        
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True