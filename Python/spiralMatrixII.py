from collections import deque
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None] * n for i in range(n)]  # initialize empty matrix 
        directions = deque([(0,1), (1,0), (0,-1), (-1,0)])  # right --> down --> left --> up
        current_number = 1
        y = 0
        x = -1
        while current_number <= n  **  2:
            y_offset, x_offset = directions.popleft() # get current direction
            while  (0 <= y + y_offset < n
                   ) and (0 <= x + x_offset < n
                   ) and (matrix[y + y_offset][x + x_offset] is None): # continue until hit non empty cell or wall
                y += y_offset
                x += x_offset
                matrix[y][x] = current_number
                current_number += 1
            directions.append((y_offset, x_offset)) # add current direction back to the end
        return matrix