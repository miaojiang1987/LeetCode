class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(len(B[0]))] for j in range(len(A))] 
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    for k in range(len(B[0])):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j] * B[j][k]
        return res