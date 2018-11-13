class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A and len(A)==0 or len(A)==1:
            return True
        
        up=False
        down=False
        
        if A[0]<=A[1]: 
            up=True
        
        if A[0]>=A[1]: 
            down=True
            
        for i in range(1,len(A)-1):
            if A[i]>A[i+1]:
                up=False
            if A[i]<A[i+1]:
                down=False
        
        return (up or down)