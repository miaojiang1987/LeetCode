class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
		# Set up start indexes for traversal
        num_rows, num_cols = len(matrix), len(matrix[0])
        start_idx = [(i, 0) for i in range(num_rows)]
        start_idx += [(num_rows - 1, j) for j in range(1, num_cols)]
        
        res = []
        is_even = True
        for r, c in start_idx:
            dia = []
            while r >= 0 and c < num_cols:
                dia.append(matrix[r][c])
                r -= 1
                c += 1
            dia = dia[::-1] if not is_even else dia
            is_even = not is_even
            res.extend(dia) 
        
        return res