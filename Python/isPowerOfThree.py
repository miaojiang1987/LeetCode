class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 1):
            return True
        if ( n == 0) :
            return False
        reminder = (n % 3)
        if (reminder == 0):
            return (self.isPowerOfThree(n / 3))
        else:
            return False