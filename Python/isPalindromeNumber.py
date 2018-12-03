class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
            
        while x > 0:
            l = x // div
            r = x % 10

            if l != r:
                return False
            x %= div
            x //= 10
            div /= 100
        return True