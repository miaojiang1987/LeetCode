class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        left=0
        right=len(A)-1
        
        result=-1
        
        while left<right:
            if A[left]+A[right]>=K:
                right-=1
            else:
                result=max(A[left]+A[right],result)
                left+=1
        
        
        return result