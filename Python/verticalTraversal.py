# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=collections.deque()
        cols={}
        row=0
        queue.append((root,0))
        
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()
                if col not in cols:
                    cols[col] = [[row, node.val]]
                else:
                    cols[col].append([row, node.val])
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
            row+=1
            
        sorted_cols = [cols[key] for key in sorted(cols.keys())]
        print(sorted_cols)
        sorted_rows=  [sorted(item) for item in sorted_cols]            
        print(sorted_rows)
        res = []
        for item in sorted_rows:
            res.append([i[1] for i in item])
        return res