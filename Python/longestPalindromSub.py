class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        dp=[[False for i in range(len(s))] for j in range(len(s))]
        maxLen = 0
        start, end = 0, 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j]=True
                
                if dp[i][j]==True:
                    if maxLen<j-i+1:
                        maxLen=j-i+1
                        start=i
                        end=j
        
        
        return s[start: start+maxLen]