class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return None
        
        #A=2*3  B=3*4 result=2*4
        
        row=len(A)
        col=len(B[0])
        res=[[0 for i in range(col)]for j in range(row)]
        
        for i in range(row):
            for j in range(len(A[0])):
                if A[i][j]!=0:
                    for k in range(len(B[0])):
                        if B[j][k]!=0:
                            res[i][k]+=A[i][j]*B[j][k]
        
        
        return res
        