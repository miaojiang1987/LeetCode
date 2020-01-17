class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for b in B:
            if b not in A:
                return -1

        A_plus = ""
        for times in range(1, len(A)+len(B)+1):
            A_plus += A
            if A_plus.find(B) != -1:
                return times
            if len(A_plus) > len(A) + len(B):
                return -1