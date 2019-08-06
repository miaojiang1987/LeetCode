class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A)==0:
            return []
        result=[]
        index=0
        for i in range(len(A)):
            if A[i]>=0:
                index=i
                break
        positive=index
        negative=index-1
        while positive<len(A) and negative>=0:
            if A[positive]**2<A[negative]**2:
                result.append(A[positive]**2)
                positive+=1
            else:
                result.append(A[negative]**2)
                negative-=1
        while negative>=0:
            result.append(A[negative]**2)
            negative-=1
        
        while positive<len(A):
            result.append(A[positive]**2)
            positive+=1
        
        return result