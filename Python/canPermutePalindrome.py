from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        counter = Counter(s)
        num_odd = 0
        for i in counter.values():
            if i % 2 == 1: num_odd += 1
        if len(s) % 2 == 1: return num_odd == 1
        return num_odd == 0