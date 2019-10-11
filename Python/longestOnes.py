class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l=0
        result=0
        count=0
        
        for i in range(len(A)):
            if A[i]==0:
                count+=1
            while count>K:
                if A[l]==0:
                    count-=1
                l+=1
            result=max(result,i-l+1)
        return result
                    
