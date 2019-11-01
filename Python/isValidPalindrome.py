class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l=0
        r=len(s)-1
        
        
        while l<=r:
            while l<=r and not s[l].isalnum():
                l+=1
            while l<=r and not s[r].isalnum():
                r-=1
            if l>r:
                return True
            
            left=s[l].lower()
            right=s[r].lower()
            if left!=right:
                return False
                
            l+=1
            r-=1
            
        
        return True