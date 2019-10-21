class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        store=0
        for i in range(len(A)-1):
            if A[i]-A[i+1]>0:
                compare=1
            elif A[i]-A[i+1]<0:
                compare=-1
            else:
                compare=0
            if compare:
                if store!=0 and compare!=0 and store!=compare:
                    return False
                store=compare
        
        
        return True
        