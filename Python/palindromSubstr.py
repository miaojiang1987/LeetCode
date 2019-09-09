class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        self.res = 0        
        n = len(s)
        for i in range(n):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res
    
    def helper(self, s, i, j):
        while i >=0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            self.res += 1