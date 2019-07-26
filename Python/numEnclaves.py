class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def dfs(r,c):
		    A[r][c] = 0
		    if r > 0 and A[r-1][c] == 1: dfs(r-1,c)
		    if r < R and A[r+1][c] == 1: dfs(r+1,c)
		    if c > 0 and A[r][c-1] == 1: dfs(r,c-1)
		    if c < C and A[r][c+1] == 1: dfs(r,c+1)
        R,C = len(A)-1,len(A[0])-1
        num1 = [[0,j] for j in range(C+1) if A[0][j] == 1]
        num1 += [[R,j] for j in range(C+1) if A[R][j] == 1]
        num1 += [[i,0] for i in range(R+1) if A[i][0] == 1]
        num1 += [[i,C] for i in range(R+1) if A[i][C] == 1]
        for i,j in num1:
            dfs(i,j)
        count = 0
        for i in range(R+1):
            count += sum(A[i])
        return count