class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if i>0 and i<len(A)-1 and A[i]>A[i-1] and A[i]>A[i+1]:
                return i