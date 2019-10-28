class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        reverse_s = s[::-1]
        for row in range(1,len(s) + 1):
            for col in range(1,len(s) + 1):
                if s[row-1] == reverse_s[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return len(s) - dp[-1][-1] <= k