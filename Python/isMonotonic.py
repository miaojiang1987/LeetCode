class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        #status={0:increasing,1:decreasing}
        
        if len(A)==1: return True
        
        i=0
        
        while i<len(A)-2:
            if A[i]<A[i+1]:
                start_trend=0
                break
            elif A[i]>A[i+1]:
                start_trend=1
                break
            i+=1
        if i==len(A)-2: return True
        for k in range(i,len(A)-1):
            if A[k]>A[k+1] and start_trend==0:
                return False
        
            if A[k]<A[k+1] and start_trend==1:
                return False
        
        return True