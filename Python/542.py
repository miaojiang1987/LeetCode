class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(matrix)
        col=len(matrix[0])
        
        answer=[[0 for i in range(col)] for j in range(row)]
        
        queue=[(x,y) for x in range(row) for y in range(col) if matrix[x][y]]
        step=0
        
        while queue:
            step += 1
            nqueue, mqueue = [], []
            for x, y in queue:
                zero = 0
                for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 0:
                        zero += 1
                if zero:
                    answer[x][y] = step
                    mqueue.append((x, y))
                else: 
                    nqueue.append((x, y))
            for x, y in mqueue:
                matrix[x][y] = 0
            queue = nqueue
        
        return answer