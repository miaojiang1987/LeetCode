class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = min(n, 10)
        dp = [1] + [9] * n  # 9 - n + 2 > 0 => 11 > n
        for i in xrange(2, n + 1):
            for x in xrange(9, 9 - i + 1, -1):
                dp[i] *= x
        return sum(dp)