class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return None
        
        m=len(A)
        n=len(A[0])
        
   
        result=[[0 for i in range(m)] for j in range(n)]
        #print(result)
      
        for x in range(m):
            for y in range(n):
                #print(A[m][n])
                result[y][x]=A[x][y]
        
        
        return result