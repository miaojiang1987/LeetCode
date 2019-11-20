class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        result=""
        words=s.split()
        for word in words:
            result+=self.reverse(word)+' '
        return result[:-1]
        
    
    def reverse(self,word):
        if not word:
            return ''
        return ''.join(reversed(word))