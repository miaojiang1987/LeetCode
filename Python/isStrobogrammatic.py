class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        
        left=0
        right=len(num)-1
        
        while left<=right:
            if num[left]==num[right]:
                if num[left]==num[right]:
                    if num[left] not in ['0', '1', '8']:
                         return False
            else:
                if (num[left]!='6' or num[right]!='9') and (num[left]!='9' or num[right]!='6'):
                    return False
            
            left+=1
            right-=1
        
        
        return True